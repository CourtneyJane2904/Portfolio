/*

    jQuery was developed independently based on flowchart provided by The Compete Web Development Course
*/
$(function()
    {
        var playing=0;
        $('#startReset').click(function()
            {
                //int data 
                let score=0,
                
                //bool data
                    //topLTdisplay returns true if the top position of elems in class fruit is less than the height of the display screen
                    //isSliced returns true if all 5 fruits have been sliced
                topLTdisplay,isSliced;
                const folder="./media/",  files=['apple.png','cherry.png','pineapple.png','strawberry.png','watermelon.png'];
                    
                let lives=["<img src='./media/heart.png' class='lives'>","<img src='./media/heart.png' class='lives'>","<img src='./media/heart.png' class='lives'>"];
            
                //indicates a game has started
                playing++;
            
            
            
                //functions used within the game
            
                //fruitSlide - controls animation of the fruit moving down the screen
                function fruitSlide()
                {
                    //fruitT is the int value of top property applied to class fruit
                    //displayH is the height of display screen
                    let fruitT=0,displayH=0;
                    
                    //ensure fruit begins back from it's orig position if it has been regenned
                    if(isSliced===true)    {$('.fruit').css('top','86px');};
                    
                    //convert returned string value from css func to int
                    displayH=parseInt($('#display').height());
                    fruitH=parseInt($('.fruit').height());
                    
                    fruitT=parseInt($('.fruit').css('top'));
                    fruitT+=Math.floor(Math.random()*30);
                    
                    //begin animation of top position from 86px to value provided by incrementing fruitT
                    $('.fruit').animate({top:fruitT});

                    //return true if top position of fruit is LT or EQ to display screen height plus the height of the fruit images
                    topLTdisplay = fruitT <= displayH+fruitH  ? true : false;        
                };
                
                //hide fruit to avoid continued play after G/O, display G/O message w/ score & refresh page after adequate reading time
                function gameOver()
                {
                    $('.fruit').hide('explode','slow');
                    clearInterval(slideFruit);
                    setTimeout(function()   { $('#gameOver').fadeIn(150);},    1050);
                    setTimeout(function()   {location.reload();},   4000);
                };
            
                //generate 5 random fruits, convert to HTML code & write code to pg
                function fruitGen()
                {
                    //show elems within class fruit in case of 1-4 fruits being sliced
                    $('.fruit').show('explode',150);
                    
                    for(var i=1;i<files.length+1;i++)
                    {
                        //create string to 5 random images within the server
                        let img=folder+files[Math.floor(Math.random()*4)],  
                        imgCode="<img src='"+img+"'>";
                        
                        //write img code to pg
                            //used  html as opposed to append to ensure previously genned fruit was removed from pg
                        $('#fruit'+i).html(imgCode);
                    };
                };
            
            
                //fill inner html of below elems with int value stored within score
                $('#GOscore').html(score);  $('#scoreVal').html(score);
                
                //refresh pg if restart button is pressed
                if(playing!==1)     {location.reload();};
                
                //alter button & lives CSS
                $('#startReset').text("Reset Game");    $('#startReset').css("width","70px");
                $('#score').show(); $('#score').css('visibility','visible');
            
                $("#livesLeft").html(lives);
                $("#livesLeft").css({'display':'block','visibility':'visible'});
                
            
                //mouse events for slicing fruit
                for(var z=1;z<files.length+1;z++)
                {
                    //begin audio of fruit slice on mouse enter
                    $('#fruit'+z).mouseenter(function()
                        {
                            //play mp3 clip if mp3 is supported, ogg otherwise
                            let audio=document.getElementById('slicesound');
                            switch(audio.canPlayType('audio/mp3'))
                            {
                                case 'probably' || 'maybe':
                                    $('#slicesound')[0].play();
                                    window.console.log('mp3 is supported');
                                    break;
                                case '':
                                    $('#slicesound')[1].play();
                                    window.console.log('mp3 is not supported');
                                    break;
                                default:
                                    $('#slicesound')[0].play();
                                    break;
                             };
                        }
                    );
                
                //create effect of fruit being sliced and increment score by 5
                     $('#fruit'+z).mouseout(function()
                        {
                            $(this).hide("explode",200);
                            score+=5;
                            $('#GOscore').html(score);  $('#scoreVal').html(score);
                        }
                    );
                };
                fruitGen();
            
                var slideFruit=setInterval(function()
                    {
                        fruitSlide();

                        //if fruit passes bottom of display screen
                            //remove a life & update html code to show this to user
                            //stop fruitSlide to avoid top position continuing to increment when moving back to it's starting position
                         if(topLTdisplay===false)
                        {
                            lives.pop();    $('#livesLeft').html(lives);
                            $('.fruit').stop();  $('.fruit').css('top','86px');
                            fruitGen(); fruitSlide();
                            if (lives.length==0)    {gameOver();};
                        } 
                             //check current display of fruit elements
                                //if all elements have been sliced (position:none), stop fruit animation and reset to orig position
                         else 
                        {
                            function ret(v) {return v=="none";}
                            let currentFruit=[];

                           for(var e=1; e<files.length+1;   e++)
                                {currentFruit.push($('#fruit'+e).css('display'));};

                            isSliced=currentFruit.every(ret);
                            if(isSliced===true)
                                {$('.fruit').stop();    fruitGen(); fruitSlide();};
                         };            

                    },500
                );     
            }
        );         
    }
);