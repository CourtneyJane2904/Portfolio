window.console.log('Hi there,');
window.console.log('this game runs off HTML and JavaScript- the JavaScript code was created entirely by myself based on gameflow logic provided by the Complete Web Development Course.');
window.console.log('Enjoy. :)');
var scoreVal=document.getElementById('scoreVal');
//game over msg
var GOscoreVal=document.getElementById('GOscore');
var GOdiv=document.getElementById('gameOver');
//correct|incorrect alerts
var rightAnswer=document.getElementById('correct');     var wrongAnswer=document.getElementById('wrong');

var question=document.getElementById('question');
/* collecting children of answers id and converting from HTML collection to array */
var ansGroup=document.getElementById('answers').children;      var ansGenned=Array.from(ansGroup);

var resetButton=document.getElementById('startReset');
//time and it's container
var counterDiv=document.getElementById('timeRemaining');   var counter=document.getElementById('time');
var gameOverV=0;

var score=0;    var gameOn=0;   var answer=0;   var y=60;
//generate new question
function quGen()
{
    if(gameOn==1)
    {
        var num=1+Math.round(Math.random()*9);   var num2=1+Math.round(Math.random()*9);
        answer=num*num2;    question.innerHTML=num+" x "+num2;

        for(var i=0;i<ansGroup.length;i++)
        {
            //generate random answers
            var Answ=Math.floor(Math.random()*100);     ansGroup[i].innerHTML=Answ;
        };

        var ansGennedBool=ansGenned.includes(answer);
        if(ansGennedBool===false)
        {
            var rand=randIndex();   var randElem=ansGroup[rand];   randElem.innerHTML=answer;
            window.console.log("Answer was not generated, replacing random value.");
        };
     };
};

//select a random index within answer group to generate answer to multiplaction
    //random to avoid predictability in location of correct answers
function randIndex()
{
    //1 taken from ansGroup.length to account for index beginning at 0
    var randInd=0;  var ansArr=ansGroup.length-1;   randInd=Math.floor(Math.random()*ansArr);
    
    if(randInd>ansArr||randInd<0)   {randInd=Math.floor(Math.random()*ansArr.length);return randInd;};
    
    return randInd;
};

//code to display relevant answer message (correct|incorrect), taking id of either as 'a' parameter
function showAns(a)
{
    //gameOn==1 stops possibility of answering qus after Game Over
    if(gameOn==1)
    {
        a.style.display="block";    setTimeout(function()   {a.style.display="none";}   ,1500);
        
        if(a==rightAnswer)  {score+=5;};
        scoreVal.innerHTML=score;
    }
}
//return 1 to be used in later comparisons
function GOval(v){return v;};

function gameOver()
{
    gameOn=0;  
    GOdiv.style.display="block";   GOscoreVal.innerHTML=score;
    gameOverV=1;GOval(gameOverV);
    
    
    setTimeout(function()  
    {
        GOdiv.style.display="none";
        counterDiv.style.visibility="hidden";   counterDiv.style.display="none";
        location.reload();
    }   ,10000);
};
resetButton.addEventListener('click',function()
    {
        counter.innerHTML=y;    gameOn++;
        //if game is started and gameOver() hasn't been called
        if(gameOn==1 && gameOverV==0)
        {
            //altering css
            counterDiv.style.visibility="visible";  counterDiv.style.display="block";
            //begin countdown from 60
            var myCounter=setInterval
            (
                function()
                {
                    y--;    counter.innerHTML=y;
                    if(y==0)   {clearInterval(myCounter);  gameOver();}
                }
            ,1000);

            resetButton.style.width="70px";
            resetButton.innerHTML="Restart Game";

            // gen new questions & answers

            quGen();

    //loop through children of answers div (possible answers) and check generated vals

        /*
        if clicked val is equiv to answer of random multiplication, perform showAns() func
        to display correct message and generate new question using quGen()

        else perform showAns on wrong msg
        */

            for(var i=0;i<ansGroup.length;i++)
            {
                 ansGroup[i].addEventListener('click',function()
                    {
                        var ansClicked=this.innerHTML;      window.console.log(ansClicked+" was clicked.");

                        if(ansClicked==answer)      {showAns(rightAnswer);  quGen();}
                        else    {showAns(wrongAnswer);}
                    }
                );

            };
        }
        //else if gameover increments over 1
        else    {location.reload();};
    }
);