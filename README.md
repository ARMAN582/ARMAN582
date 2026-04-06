<!DOCTYPE html>
<html lang="en">
<head>

<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>ArmanQureshi Market Cards</title>

<style>

body{
margin:0;
background:#000;
color:white;
font-family:Arial;
overflow-x:hidden;
}

/* background */

canvas{
position:fixed;
top:0;
left:0;
width:100%;
height:100%;
z-index:-1;
}

/* header */

header{
text-align:center;
padding:30px;
}

.mainTitle{
font-size:52px;
letter-spacing:6px;
color:#00ffcc;
text-shadow:0 0 20px #00ffcc;
}

/* profit loss */

.marketSummary{
display:flex;
justify-content:center;
gap:20px;
margin-top:15px;
flex-wrap:wrap;
}

.box{
background:#111;
padding:12px 20px;
border-radius:10px;
font-size:18px;
box-shadow:0 0 10px #00ffcc40;
}

#totalProfit{color:lime;}
#totalLoss{color:red;}

/* buttons */

.btn{
padding:10px 18px;
margin:5px;
border-radius:25px;
text-decoration:none;
font-weight:bold;
display:inline-block;
}

.whatsapp{background:#25D366;color:black;}
.instagram{background:#E1306C;color:white;}
.facebook{background:#1877F2;color:white;}
.snapchat{background:#FFFC00;color:black;}

/* section */

.section{
text-align:center;
padding:30px;
}

/* GRID FIX (important) */

.cards{
display:grid;
grid-template-columns:repeat(auto-fit,220px);
gap:25px;
justify-content:center;
}

/* card container */

.card-container{
width:220px;
height:300px;
perspective:1000px;
position:relative;
}

.card-container.active{
z-index:100;
}

/* card */

.card{
width:100%;
height:100%;
position:relative;
transform-style:preserve-3d;
transition:transform 0.7s;
cursor:pointer;
}

.card-container.active .card{
transform:rotateY(180deg);
}

/* faces */

.card-front,
.card-back{
position:absolute;
top:0;
left:0;
width:100%;
height:100%;
border-radius:15px;
backface-visibility:hidden;
overflow:hidden;
box-shadow:0 0 20px rgba(0,255,0,0.4);
}

/* front */

.card-front{
background-size:cover;
background-position:center;
position:relative;
}

/* icon */

.assetIcon{
position:absolute;
top:10px;
left:10px;
font-size:28px;
}

/* name overlay */

.overlay{
position:absolute;
bottom:0;
width:100%;
background:linear-gradient(transparent,rgba(0,0,0,0.9));
text-align:center;
padding:12px;
}

.overlay span{
font-size:20px;
letter-spacing:3px;
color:#00ffcc;
text-shadow:0 0 10px #00ffcc;
font-weight:bold;
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

<canvas id="bg"></canvas>

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

<a class="btn whatsapp" href="https://wa.me/9026550240">WhatsApp</a>
<a class="btn instagram" href="https://instagram.com/armanqureshi2800">Instagram</a>
<a class="btn facebook" href="https://www.facebook.com/share/19pPMX9SMV/">Facebook</a>
<a class="btn snapchat" href="https://www.snapchat.com/add/armanqureshi_28">Snapchat</a>

</header>

<section class="section">

<h2>Live Market Cards</h2>

<div class="cards" id="cards"></div>

</section>

<script>

/* assets */

const assets=[
"Gold","Silver","Bitcoin","Ethereum","Adani Power",
"Adani Green","Adani Ports","Reliance","Tata Steel",
"Infosys","Wipro","HDFC","ICICI","ONGC",
"Crude Oil","Natural Gas","Coal India","BSNL",
"Vodafone Idea","Sensex","Nifty","Bank Nifty",
"Gasoline","Petrol","Diesel","Adani Gas",
"Tata Motors","Jio","Crypto Index","Silver Future","Gold Future"
]

/* icons */

const icons=[
"🥇","🥈","₿","Ξ","⚡",
"🌱","🚢","📊","🏭",
"💻","💻","🏦","🏦","⛽",
"🛢","🔥","⛏","📡",
"📶","📈","📉","🏦",
"⛽","⛽","🚛","🔥",
"🚗","📱","🪙","🥈","🥇"
]

const wrapper=document.getElementById("cards")

assets.forEach((a,i)=>{

let container=document.createElement("div")
container.className="card-container"

let card=document.createElement("div")
card.className="card"

card.onclick=function(e){

e.stopPropagation()

container.classList.toggle("active")

}

/* front */

let front=document.createElement("div")
front.className="card-front"
front.style.backgroundImage=`url(photo${i+1}.jpg)`

front.innerHTML=`

<div class="assetIcon">${icons[i]}</div>

<div class="overlay">
<span>ARMANQURESHI</span>
</div>

`

/* back */

let back=document.createElement("div")
back.className="card-back"

back.innerHTML=`
<h3>${a}</h3>
<div class="price" id="price${i}">₹0</div>
<div class="change" id="change${i}">Loading...</div>
`

card.appendChild(front)
card.appendChild(back)

container.appendChild(card)
wrapper.appendChild(container)

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

/* particles */

const canvas=document.getElementById("bg")
const ctx=canvas.getContext("2d")

canvas.width=window.innerWidth
canvas.height=window.innerHeight

let particles=[]

for(let i=0;i<120;i++){

particles.push({
x:Math.random()*canvas.width,
y:Math.random()*canvas.height,
r:Math.random()*3,
s:Math.random()*0.5
})

}

function animate(){

ctx.clearRect(0,0,canvas.width,canvas.height)

particles.forEach(p=>{

p.y-=p.s
if(p.y<0)p.y=canvas.height

ctx.beginPath()
ctx.arc(p.x,p.y,p.r,0,Math.PI*2)
ctx.fillStyle="rgba(0,255,0,0.7)"
ctx.fill()

})

requestAnimationFrame(animate)

}

animate()

</script>

</body>
</html>
