<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<!-- Enforce Content Security Policy to secure inline scripts and styles and restrict external resource access -->
<meta http-equiv="Content-Security-Policy" content="default-src 'self'; style-src 'unsafe-inline'; script-src 'unsafe-inline'; img-src 'self' data:; connect-src 'self';">

<title>ArmanQureshi Market Cards</title>

<style>

body{
margin:0;
font-family:Arial;
background:#000;
color:white;
overflow-x:hidden;
}

/* header */

header{
text-align:center;
padding:25px;
}

.mainTitle{
font-size:48px;
letter-spacing:6px;
color:#00ffc8;
text-shadow:0 0 20px #00ffc8;
}

.marketSummary{
display:flex;
justify-content:center;
gap:20px;
margin-top:10px;
flex-wrap:wrap;
}

.box{
background:#111;
padding:10px 20px;
border-radius:10px;
font-size:18px;
}

#totalProfit{color:lime;}
#totalLoss{color:red;}

/* buttons */

.social{
margin-top:15px;
}

.btn{
padding:8px 16px;
margin:5px;
border-radius:20px;
text-decoration:none;
font-weight:bold;
display:inline-block;
}

.whatsapp{background:#25D366;color:black;}
.instagram{background:#E1306C;color:white;}
.facebook{background:#1877F2;color:white;}
.snapchat{background:#FFFC00;color:black;}

/* cards grid */

.cards{
display:grid;
grid-template-columns:repeat(auto-fit,220px);
gap:25px;
justify-content:center;
padding:30px;
}

/* card */

.card-container{
width:220px;
height:300px;
perspective:1000px;
}

.card{
width:100%;
height:100%;
position:relative;
transform-style:preserve-3d;
transition:transform .6s;
cursor:pointer;
}

.card.flip{
transform:rotateY(180deg);
}

/* faces */

.card-face{
position:absolute;
width:100%;
height:100%;
border-radius:15px;
backface-visibility:hidden;
overflow:hidden;
box-shadow:0 0 20px rgba(0,255,200,.3);
}

/* front */

.card-front{
background-size:cover;
background-position:center;
}

.overlay{
position:absolute;
bottom:0;
width:100%;
background:linear-gradient(transparent,rgba(0,0,0,.9));
text-align:center;
padding:10px;
}

.overlay span{
letter-spacing:3px;
font-weight:bold;
color:#00ffc8;
}

/* back */

.card-back{
background:#111;
transform:rotateY(180deg);
display:flex;
flex-direction:column;
align-items:center;
justify-content:center;
}

.price{
font-size:26px;
color:#FFD700;
}

.change{
font-size:18px;
margin-top:6px;
}

</style>
</head>

<body>

<header>

<h1 class="mainTitle">ARMANQURESHI</h1>

<div class="marketSummary">

<div class="box">
Total Profit ₹ <span id="totalProfit">0</span>
</div>

<div class="box">
Total Loss ₹ <span id="totalLoss">0</span>
</div>

</div>

<div class="social">
<a class="btn whatsapp" href="https://wa.me/9026550240" target="_blank" rel="noopener noreferrer">WhatsApp</a>
<a class="btn instagram" href="https://instagram.com/armanqureshi2800" target="_blank" rel="noopener noreferrer">Instagram</a>
<a class="btn facebook" href="https://www.facebook.com/share/19pPMX9SMV/" target="_blank" rel="noopener noreferrer">Facebook</a>
<a class="btn snapchat" href="https://www.snapchat.com/add/armanqureshi_28" target="_blank" rel="noopener noreferrer">Snapchat</a>
</div>

</header>

<div class="cards" id="cards"></div>

<script>

/* asset names */

const assets=[
"Gold","Silver","Bitcoin","Ethereum","Adani Power",
"Adani Green","Adani Ports","Reliance","Tata Steel",
"Infosys","Wipro","HDFC","ICICI","ONGC",
"Crude Oil","Natural Gas","Coal India","BSNL",
"Vodafone Idea","Sensex","Nifty","Bank Nifty",
"Gasoline","Petrol","Diesel","Adani Gas",
"Tata Motors","Jio","Crypto Index","Silver Future","Gold Future"
]

const cards=document.getElementById("cards")

/* create cards */

assets.forEach((asset,i)=>{

let container=document.createElement("div")
container.className="card-container"

let card=document.createElement("div")
card.className="card"

card.onclick=()=>{
card.classList.toggle("flip")
}

let front=document.createElement("div")
front.className="card-face card-front"
front.style.backgroundImage=`url(photo${i+1}.jpg)`

front.innerHTML=`
<div class="overlay">
<span>ARMANQURESHI</span>
</div>
`

let back=document.createElement("div")
back.className="card-face card-back"

back.innerHTML=`
<h3>${asset}</h3>
<div class="price" id="price${i}">₹0</div>
<div class="change" id="change${i}">Loading...</div>
`

card.appendChild(front)
card.appendChild(back)

container.appendChild(card)
cards.appendChild(container)

})

/* market simulation */

let prices=[]
function updateMarket(){

let totalProfit=0
let totalLoss=0

assets.forEach((a,i)=>{

if(!prices[i]) prices[i]=Math.random()*1000+100

let move=(Math.random()-0.5)*20

prices[i]+=move

document.getElementById("price"+i).innerText="₹"+prices[i].toFixed(2)

let change=document.getElementById("change"+i)

if(move>0){

change.innerHTML="▲ Profit "+move.toFixed(2)
change.style.color="lime"
totalProfit+=move

}else{

change.innerHTML="▼ Loss "+move.toFixed(2)
change.style.color="red"
totalLoss+=Math.abs(move)

}

})

document.getElementById("totalProfit").innerText=totalProfit.toFixed(2)
document.getElementById("totalLoss").innerText=totalLoss.toFixed(2)

}

setInterval(updateMarket,2000)

</script>

</body>
</html>
