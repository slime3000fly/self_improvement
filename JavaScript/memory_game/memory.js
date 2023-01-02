var pairs = ["ciri.png","geralt.png","jaskier.png","jaskier.png",
"iorweth.png","triss.png","geralt.png","yen.png","ciri.png","triss.png","yen.png","iorweth.png"];
var cards = [];
var cardNumber = 12;


while (pairs.length != 0)
{
    number = Math.floor(Math.random() * cardNumber);
    cards.push(pairs[number])
    pairs.splice(number,1)
    cardNumber --;
}


for (let i = 0; i < cards.length; i++)
{
    var divNumber = "c" + i
    var divNumber = document.getElementById(divNumber);
    divNumber.addEventListener("click",function(){revealCard(i);});
} 


var oneVisible = false;
var turnCounter = 0;
var previos_nr;
var lock = false;
var parisLeft = 6;

function revealCard(nr)
{
    var opacityValue = $('#c'+nr).css('opacity');
    console.log(opacityValue);
    if (opacityValue != 0 && lock ==false)
    {
        lock = true;
        // alert(nr)
    var obraz = "url(img/" + cards[nr]+")";

    $('#c'+ nr).css('background-image',obraz);
    $('#c'+ nr).addClass('cardA');
    $('#c'+ nr).removeClass('card');

    if(oneVisible == false)
    {
        //first card
        
        oneVisible = true;
        previos_nr = nr;
        lock = false;
    }
    else
    {
        //second card

        if(cards[previos_nr]==cards[nr])
        {
            // alert("para");
            setTimeout(function() {hide2cards(nr,previos_nr)},750);
        }
        else
        {
            setTimeout(function() {restore2cards(nr,previos_nr)},1000);
            
        }
        
        turnCounter ++;
        $('.score').html('Turn counter: '+ turnCounter);
        oneVisible = false;
    }
    }

    
}

function hide2cards(nr1,nr2)
{
    $('#c'+nr1).css('opacity','0');
    $('#c'+nr2).css('opacity','0');
    
    parisLeft --;
    if (parisLeft ==0)
    {
        $('.board').html('<h1>You Win<br>Done in ' +turnCounter + 
        ' turns</br></h1> <button type="button" onclick="window.location.reload();" class ="button">Restart</button>')
    }

    lock = false;
    
}

function restore2cards(nr1,nr2)
{
    $('#c'+ nr1).css('background-image','url(img/karta.png)');
    $('#c'+ nr1).addClass('card');
    $('#c'+ nr1).removeClass('cardA');

    $('#c'+ nr2).css('background-image','url(img/karta.png)');
    $('#c'+ nr2).addClass('card');
    $('#c'+ nr2).removeClass('cardA');
    lock = false;
}