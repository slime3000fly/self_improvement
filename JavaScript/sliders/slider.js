//javascript code which change slide on page

var script = document.createElement('script');
script.src = 'https://code.jquery.com/jquery-3.6.0.min.js';
document.getElementsByTagName('head')[0].appendChild(script);

var slide_number = 1;
const number_of_slides = 5;

function hide()
{
    $("#slider").fadeOut(500);
}

function change_slide()
{
    if (slide_number == number_of_slides)
    {
        slide_number = 1;
    }
    slide_number ++;

    var slide = "<img src=\"slide" + slide_number + ".jpg\" id=\"image\"/>";
    

    document.getElementById("slider").innerHTML = slide
    $("#slider").fadeIn(500)

    
    setTimeout(change_slide,5000);
    setTimeout(hide,4500);
}