/*
This is code I produced following along to OpenGL's Getting Started tutorials up until Hello Triangle
https://learnopengl.com/Getting-started/OpenGL

It's just a mess of code and commentd as my main purpose was to get acquainted with the basics of OpenGL
renders a rectangle in it's current state but can be adjusted to render a triangle too 
	I've specified in comments what code to comment out if this is desired
*/

#include <glad.h>
#include <glfw3.h>
#include <iostream>
#include <vector>
/*
first step is to link glad and glfw3 to the project by adjusting project's include and lib dirs accordingly
*/

/*
a vertex shader
	where we declare all input vertex attributes

as we only care about position data currently. we only need a single vertex attribute
*/
const char *vertexShaderSource = "#version 330 core\n"
    "layout (location = 0) in vec3 aPos;\n"
    "void main()\n"
    "{\n"
    "   gl_Position = vec4(aPos.x, aPos.y, aPos.z, 1.0);\n"
	"}\0";

/*
fragment shader
	calculates colour output for pixels
*/

const char* fragmentShaderSource = "#version 330 core\n"
"out vec4 FragColor;\n"
"void main()\n"
"{\n"
"FragColor = vec4(1.0f, 0.5f, 0.2f, 1.0f);\n"
"}\0";

/*
a function for processing input
*/
void processInput(GLFWwindow* window) 
{
	// if escape key is in state PRESS
	if (glfwGetKey(window, GLFW_KEY_ESCAPE) == GLFW_PRESS) 
	{
		// set WindowShouldClose to true, will be acted on in next iteration of render loop
		glfwSetWindowShouldClose(window, true);
	}
}

/*
adjust viewport when window is resized by user
done by registering a callback function with specific prototype
*/
void framebuffer_size_callback(GLFWwindow* window, int width, int height)
{
	// adjusts window size to passed-in width and height
	glViewport(0, 0, width, height);
}

int main() 
{
	// instantiate the GLFW window
	glfwInit();
	// set values of GLFW_CONTEXT_VERSION_*  variables
	glfwWindowHint(GLFW_CONTEXT_VERSION_MAJOR, 3);
	glfwWindowHint(GLFW_CONTEXT_VERSION_MINOR, 3);
	// set profile of OpenGL to core
	glfwWindowHint(GLFW_OPENGL_PROFILE, GLFW_OPENGL_CORE_PROFILE);

	/*
	input vertex data
	coordinates in 3D as OpenGL works with 3D mainly

	only processes 3D coordinates in a specific range between -1.0 and 1.0
		called normalized device coordinates range

	rendering a single triangle means we need to specify 3 vertices (sides)
	*/

	/* 
	vertices[] definition when drawing a single triangle- comment this out in case of triangle
	
	float vertices[] =
	{	//x		 y		z
		-0.5f, -0.5f, 0.0f,
		 0.5f, -0.5f, 0.0f,
		 0.0f,	0.5f, 0.0f
	};
	*/

	/*
	To draw a rectangle instead of a square, we would need 6 vertices if we used vertices alone
	this would work but would cause overlap on the bottom right and top lwft
		a problem when rendering several triangles

	To allow the drawing of a rectangle using only 4 vertices (as expected,) we need to use
		an Element Buffer Object
			a buffer that stores indices that OpenGL uses to decide what vertices to draw
				called indexed drawing

	without using an EBO, we would need to draw a rectangle using 6 vertices, 2 of which are duplicated:

	float vertices[] = {
		// first triangle
		  x	      y		z
		 0.5f,  0.5f, 0.0f,  // top right
		 0.5f, -0.5f, 0.0f,  // bottom right
		-0.5f,  0.5f, 0.0f,  // top left
		// second triangle
		 0.5f, -0.5f, 0.0f,  // bottom right	->	copied
		-0.5f, -0.5f, 0.0f,  // bottom left
		-0.5f,  0.5f, 0.0f   // top left		->  copied
	};

	comment out below definition of vertices[] and indices[] if single triangle desired
	*/

	float vertices[] =
	{
		0.5f,  0.5f, 0.0f,	// top right
		0.5f, -0.5f, 0.0f,	// bottom right
	   -0.5f, -0.5f, 0.0f,  // bottom left
	   -0.5f,  0.5f, 0.0f   // top left
	};

	unsigned int indices[] =
	{
		0, 1, 3,	// first triangle- use first, second and fourth vertices
		1, 2, 3		// second triangle- use second, third and fourth vertices
	};

	
	// create a window object
	GLFWwindow* window = glfwCreateWindow(800, 600, "LearnOpenGL", NULL, NULL);
	if (window == NULL) 
	{
		// error checking for window creation- exits if it fails
		std::cout << "Failed to create GLFW window";
		glfwTerminate();
		return -1;
	}
	glfwMakeContextCurrent(window);

	// initialize GLAD before calling any OpenGL functions as it manages func pointers for OpenGL
	if (!gladLoadGLLoader((GLADloadproc)glfwGetProcAddress)) 
	{
		// if glad initialization fails, exit is triggered
		std::cout << "Failed to initialize GLAD." << std::endl;
		return -1;
	}

	/*
	create shader object referenced by id

	GL_VERTEX_SHADER:	specifies the shader type
	*/
	unsigned int vertexShader;
	vertexShader = glCreateShader(GL_VERTEX_SHADER);

	/*
	attach shader src code to shader object
	compile shader

	glShaderSource -> compiles shader object
	@param shaderToCompile
	@param stringsPassedAsSrc
	*/
	glShaderSource(vertexShader, 1, &vertexShaderSource, NULL);
	glCompileShader(vertexShader);

	/*
	error checking for shader compilation
	integer used to indicate success
	*/
	int success;
	// storage for error messages
	char infoLog[512];
	// check if compilation was a success
	glGetShaderiv(vertexShader, GL_COMPILE_STATUS, &success);

	if (!success)
	{
		glGetShaderInfoLog(vertexShader, 512, NULL, infoLog);
		std::cout << "Shader compilation failed.\n" << infoLog << std::endl;
	}

	/*
	compiling the fragment shader
	similar to compiling vertex shader with the exception of specifying the shader type as
		GL_FRAGMENT_SHADER
	*/
	unsigned int fragmentShader;
	fragmentShader = glCreateShader(GL_FRAGMENT_SHADER);
	glShaderSource(fragmentShader, 1, &fragmentShaderSource, NULL);
	glCompileShader(fragmentShader);

	/*
	link compiled shaders into a shader program and activate when rendering objects
	activated shader program's shaders used when issuing render calls

	linking shaders into a program links outputs of each shader to inputs of next
	*/

	unsigned int shaderProgram;
	// creates program and returns ID to new program
	shaderProgram = glCreateProgram();

	// attach compiled shaders to program 
	glAttachShader(shaderProgram, vertexShader);
	glAttachShader(shaderProgram, fragmentShader);
	glLinkProgram(shaderProgram);

	// error checking for shader program linking
	glGetProgramiv(shaderProgram, GL_LINK_STATUS, &success);
	if (!success) {
		glGetProgramInfoLog(shaderProgram, 512, NULL, infoLog);
		std::cout << "failed to link shader program.\n" << infoLog << std::endl;
	}

	// delete shader objects now as we have them in the program
	glDeleteShader(vertexShader);
	glDeleteShader(fragmentShader);
	
	/*
	generate a vertex buffer object (VBO) with a buffer ID
		creates memory on GPU where we store vertex data
		config how OpenGL should interpret memory
		specify how to send data to graphics card
	*/
	unsigned int VAO;
	glGenVertexArrays(1, &VAO);

	unsigned int VBO;
	glGenBuffers(1, &VBO);

	/*
	creating the EBO
	*/
	unsigned int EBO;
	glGenBuffers(1, &EBO);

	/*
	vertex array object (VAO) 
	needed so OpenGL knows what to do with vertex inputs

	stored:
		calls to manipulate VertexAttribArray
		vertex attribute configs via VertexAttribPointer
		VBOs associated with vertex attributes
	*/

	//bind VAO
	glBindVertexArray(VAO);

	/*
	buffer type of a VBO is GL_ARRAY_BUFFER
	can bind to several buffers at once as long as they have different buffer types
	*/
	glBindBuffer(GL_ARRAY_BUFFER, VBO);
	glBufferData(GL_ARRAY_BUFFER, sizeof(vertices), vertices, GL_STATIC_DRAW);


	/*
	bind the EBO and copy indices into buffer with glBufferData
	comment out if triangle desired 
	*/
	glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, EBO);
	glBufferData(GL_ELEMENT_ARRAY_BUFFER, sizeof(indices), indices, GL_STATIC_DRAW);

	// tell OpenGL how to interpret vertex data 
	/*
	glVertexAttribPointer
	@param first -> which vertex attribute to config (spwcified by location attribute in vertex shader
	@param second -> size of vertex attribute- vec3 means 3 vals
	@param third -> type of data
	@param fourth -> should data be normalized?
	@param fifth -> stride, tells us space between vertex attributes
					3 as there are 3 floats in a vertex
	@param sixth -> offset where position cata begins in buffer
					position data is at start of data array so is 0
	*/
	glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 3 * sizeof(float), (void*)0);
	glEnableVertexAttribArray(0);
	/*
	from bind, any buffer calls we make on GL_ARRAY_BUFFER target will be
	used to config the bound buffer (VBO)

	glBufferData() -> copies previously defined vertex data into buffer's memory
	@param bufferType
	@param sizeOfData
	@param dataToSend
	@param howToManageData
		GL_STREAM_DRAW: data is set once and used only a few times
		GL_STATIC_DRAW:	data is set once and used many times
		GL_DYNAMIC_DRAW: data is changed frequently and used many times
	*/
	glBindBuffer(GL_ARRAY_BUFFER, 0);

	// tell openGL the size of the rendering window
	// here is how OpenGL knows how we want to display data and coords with respect to window
	
	// NOTE: show match the width and height given above to glfwCreateWindow
	glViewport(0, 0, 800, 600);

	// register framebuffer_size_callback as callback for window resizing
	glfwSetFramebufferSizeCallback(window, framebuffer_size_callback);
	
	/*
	the render loop
	keeps running until we tell GLFW to stop

	glfwWindowShouldClose() -> checks if GLFW has been instructed to close,
							   returning true if so
	*/

	while (!glfwWindowShouldClose(window)) 
	{
		/*
		call processInput to check for user input before rendering grsphivd
		*/
		processInput(window);

		/*
		clear screen with colour of choice to check things are working
		
		renders screen with green-blueish background
		*/
		glClearColor(0.2f, 0.3f, 0.3f, 1.0f);
		glClear(GL_COLOR_BUFFER_BIT);
		// activate created program, use when we want to render that object
		glUseProgram(shaderProgram);
		glBindVertexArray(VAO);
		
		/* use if drawing triangles without the use of EBO
		 glDrawArrays(GL_TRIANGLES, 0, 3);
		*/

		// use drawElements to indicate that truangles should be rendered from index buffer
		// aka. draw using indices in currently bound EBO
		glDrawElements(GL_TRIANGLES, 6, GL_UNSIGNED_INT, 0);
		//glBindVertexArray(0);
		/* 
		swaps the colour buffer 
			a large 2D buffer containing colour values for each pixel in window
		*/
		glfwSwapBuffers(window);
		/* 
		checks if any events have been triggered (keyboard input | mouse), updates
		window state and calls corresponding callback function
		*/
		glfwPollEvents();
	}

	/*
	clean/delete all of GLFW's resources that were allocated
	*/
	glfwTerminate();

	return 0;
}
