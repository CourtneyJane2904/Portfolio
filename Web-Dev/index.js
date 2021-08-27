var slide,num,click=0;
$(function()
    {
        $('html').fadeIn(1000);
    }
 );
$('#slideshowT').click(function()
    {
        
        var imgs=["./media/me.jpg","./media/ateb-logo.png","./media/north it.png"],num=0;
        if(click==0)
        {click++,
            slide=setInterval(function()
            {
                
                $("#aboutImgs").fadeOut(1500,function()
                {
                    var thisIsDup=($("#aboutImgs").attr("src") == imgs[num]) ? true : false;
                    
                    if(thisIsDup)    {$("#aboutImgs").attr("src","./img1.jpg");}
                    else    {$("#aboutImgs").attr("src",imgs[num]);};
                    
                   if(num>2)    {num=0;$("#aboutImgs").attr("src",imgs[num]);};
                    num++;
                });
                $("#aboutImgs").fadeIn(1500);
            }
        ,6000
        );};
    }
    );
$('#slideshowT').siblings().click(function()
    {
        clearInterval(slide);click=0;
    }
);
$('.nav-link.tabs').click(function()
    {
        var collThis=$(this).attr('href').substring();
        $(collThis).toggleClass('active');
        $(collThis).collapse('toggle');
        window.console.log(collThis);
    
        var t=setTimeout(function()
        {
            if($('.tab-pane').hasClass('active'))
            {
                $('#contentWhenColled').hide();
                $(collThis).siblings().removeClass('active');
            }
            else
            {
                $('#contentWhenColled').show();
            };
        },200);
        
        
    }
);






