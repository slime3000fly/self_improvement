var word = "Javascript";
word = word.toUpperCase();

var length = word.length;
var wrong = 0

var word1 = "";//hiden word

for (i = 0; i < length; i++) 
{
    if (word.charAt(i) == " ") word1 = word1 + " ";
    else word1 = word1 + "-";

}

// word1 = "dsfhgdsfsdg"

function write_word()
{
    document.getElementById("word").innerHTML = word1;
}

window.onload = start;

var letters_in_alphabet = new Array(26);

letters_in_alphabet[0] = "A";
letters_in_alphabet[1] = "B";
letters_in_alphabet[2] = "C";
letters_in_alphabet[3] = "D";
letters_in_alphabet[4] = "E";
letters_in_alphabet[5] = "F";
letters_in_alphabet[6] = "G";
letters_in_alphabet[7] = "H";
letters_in_alphabet[8] = "I";
letters_in_alphabet[9] = "J";
letters_in_alphabet[10] = "K";
letters_in_alphabet[11] = "L";
letters_in_alphabet[12] = "M";
letters_in_alphabet[13] = "N";
letters_in_alphabet[14] = "O";
letters_in_alphabet[15] = "P";
letters_in_alphabet[16] = "Q";
letters_in_alphabet[17] = "R";
letters_in_alphabet[18] = "S";
letters_in_alphabet[19] = "T";
letters_in_alphabet[20] = "U";
letters_in_alphabet[21] = "V";
letters_in_alphabet[22] = "W";
letters_in_alphabet[23] = "X";
letters_in_alphabet[24] = "Y";
letters_in_alphabet[25] = "Z";



function start() 
{

    var div_content = "";

    for (i = 0; i < 26; i++)
    {
        var element = "letter" + i;
        div_content = div_content + '<div class="letter" onclick="check(' + i + ')" id ="' + element + '">' + letters_in_alphabet[i] + '</div>';
        if ((i + 1) % 7 == 0) div_content = div_content + '<div style = clear:both;></div>';
    }

    document.getElementById("alphabet").innerHTML = div_content;

    write_word();
}

String.prototype.changeChar = function (place, char)
{
    if (place > this.length - 1) return this.toString();
    else return this.substr(0, place) + char + this.substr(place + 1);
}

function check(number)
{
    var hit = false;

    for (i = 0; i < length; i++)
    {
        if (word.charAt(i) == letters_in_alphabet[number])
        {
            word1 = word1.changeChar(i, letters_in_alphabet[number]);
            hit = true;
        }
    }

    if (hit == true)
    {
        var element = "letter" + number
        document.getElementById(element).style.background = "green";
        document.getElementById(element).style.color = "#00C000";
        document.getElementById(element).style.border = "3px solid #00C000";
        document.getElementById(element).style.cursor = "default";

        write_word();
    }
    else
    {
        var element = "letter" + number
        document.getElementById(element).style.background = "#330000";
        document.getElementById(element).style.color = "#C00000";
        document.getElementById(element).style.border = "3px solid #C00000";
        document.getElementById(element).style.cursor = "default";
        document.getElementById(element).setAttribute("onclick", ";");

        //wrong letter
        wrong++;
        var image = "img/s" + wrong + ".jpg"
        document.getElementById("hangman").innerHTML = '<img src="' + image + '"alt=""/>'
    }

    //win
    if (word == word1)
    {
        document.getElementById("alphabet").innerHTML = "YOU WON!!!" + '<br/><br/><span class="reset" onclick="location.reload()">Again?</span>';
    }

    //lose
    if (wrong >= 9)
    {
        document.getElementById("alphabet").innerHTML = "YOU DIE. Word was: " + word + '<br/><br/><span class="reset" onclick="location.reload()">Again?</span>';
    }
}