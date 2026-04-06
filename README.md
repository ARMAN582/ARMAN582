<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Arman Qureshi | Live Market Cards</title>

<style>

body{
margin:0;
background:#000;
color:white;
font-family:Arial;
overflow-x:hidden;
}

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

h1{
font-size:48px;
margin:0;
}

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

.section{
text-align:center;
padding:30px;
}

.cards{
display:flex;
flex-wrap:wrap;
justify-content:center;
gap:20px;
}

/* ATM Card */

.card-container{
perspective:1000px;
}

.card{
width:220px;
height:300px;
position:relative;
transform-style:preserve-3d;
transition:0.8s;
}

.card:hover{
transform:rotateY(180deg);
}

.card-front,
.card-back{

position:absolute;
width:100%;
height:100%;
border-radius:15px;
backface-visibility:hidden;
overflow:hidden;
box-shadow:0 0 20px rgba(0,255,0,0.4);
}

.card-front{
background-size:cover;
background-position:center;
}

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

<h1>Arman Qureshi</h1>

<a class="btn whatsapp" href="https://wa.me/9026550240">WhatsApp</a>
<a class="btn instagram" href="https://instagram.com/armanqureshi2800">Instagram</a>
<a class="btn facebook" href="#">Facebook</a>
<a class="btn snapchat" href="#">Snapchat</a>

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

/* cards */

const wrapper=document.getElementById("cards")

assets.forEach((a,i)=>{

let container=document.createElement("div")
container.className="card-container"

let card=document.createElement("div")
card.className="card"

let front=document.createElement("div")
front.className="card-front"
front.style.backgroundImage=`url(photo${i+1}.jpg)`

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

/* fake market movement */

let prices=[]

function updateMarket(){

assets.forEach((a,i)=>{

if(!prices[i]) prices[i]=Math.random()*1000+100

let move=(Math.random()-0.5)*20

prices[i]+=move

let price=prices[i].toFixed(2)

document.getElementById("price"+i).innerText="₹"+price

let change=document.getElementById("change"+i)

if(move>0){

change.innerHTML="▲ Profit "+move.toFixed(2)
change.style.color="lime"

}else{

change.innerHTML="▼ Loss "+move.toFixed(2)
change.style.color="red"

}

})

}

setInterval(updateMarket,2000)

/* particle background */

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
