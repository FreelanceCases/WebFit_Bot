require("dotenv").config();
const express = require('express');
const DB=require("./additional/database")
const V_S=require("./files/Stream/video_share")
const cc=require('./files/contentchecker')
const additional=require('./files/Additional')
const app = express();
const bodyParser = require('body-parser');
const {NotifyUser} = require("./additional/database");
const {mark_comment, get_prim_training,mark_ex} = require("./GoogleTables/parcer");

app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());
app.use(express.urlencoded({ extended: false }));
app.use(express.json());


const server_url = process.env.SERVER_URL;
const path_for_trainings = process.env.PATH_FOR_TRAINING;


app.get('/video/:id', async (req, res) => {
 console.log("Админ просматривает видео")
 const mobile_number=req.params.id
 var date=Number(await DB.geDate(mobile_number))-1
 try{final_path=await additional.re(mobile_number,date,false)
  if (final_path=="No"){res.send("No video")}
  else{V_S.CreateStream(req,res,final_path)}}
 catch (e){
  console.log(e)
  console.log("все")
 }


 });

app.get("/videowatchingbytrainer/:number/:date/:name",async (req,res)=>{
 console.log("Пользователь смотрит видео по гиперссылке")
 const url= path_for_trainings + "/"+req.params.number+"/"+req.params.date+"/"+req.params.name
 console.log(url)
 V_S.CreateStream(req,res,url)
})
app.post("/mobile/:id", async (req,res,next)=>{
 console.log("Фильтрация видео")
 params=req.params.id.toString()
 message=req.body
 cc.metrica(params,message["value_or_plus"],message["commentario"])
});

app.post("/commentere",async (req,res)=>{
 console.log("Пользователь оставил комментарий")
 message=req.body //google_sheets //date //type //comm
 console.log(message)
 try{
 mark_comment(message["ex"],message["date"],message["comm"],message["googlesheets"],message["exnum"],message["newval"])
 res.send("ok")}
 catch (e){
  res.send(e.toString())
 }

})

app.post("/markex",async (req,res)=> {
 console.log("Пользователь отметил выполнение тренировки")
 message = req.body //google_sheets //date //type //comm
 console.log(message)
 try {
  mark_ex(message["ex"], message["date"], message["googlesheets"], message["exnum"], message["col"])
  res.send("ok")
 } catch (e) {
  res.send(e.toString())
 }
})
app.post("/mobileapplication", async (req,res,next)=>{
 console.log("Парметры пользователя обновлены")
 message=req.body
 NotifyUser(message["mobile"],message["approved"])
 DB.UpdateProperties("approved", message["approved"],message["mobile"])
 DB.UpdateProperties("diete",message["diete"],message["mobile"])
 DB.UpdateProperties("googleforms",message["googleforms"],message["mobile"])
 DB.UpdateProperties("date",message["payment"],message["mobile"])
 res.json("OK")
 next();
});
app.get("/getTrain/:id/:mobile",async (req,res)=>{
 googletable=req.params.id.toString()
 mobile=req.params.mobile.toString()
 console.log(req.params)
 console.log("Была запрошена вся тренировка из гугл таблицы")
 massive=await get_prim_training(googletable,mobile)
 console.log(massive)
  res.send(massive)
})

app.get("/mobileapplication", async (req, res, next)=>{
 console.log("Showing all users")
 res.setHeader("content-type","application/json")
 res.json(await DB.getUsers())})



//
// while (true) {
//  try {
//   app.listen(3000,"192.168.1.30",()=> {
//    console.log("Server Launched!")
//    setInterval(cc.starter,30000)//Проверять каждые 30 секунд новые видео
//
//   })
//  } catch (e) {
//   console.log(e.toString())
//  }
// }
//

 app.listen(3000, server_url,()=> {
  console.log("Server Launched!")
  setInterval(cc.starter,30000)//Проверять каждые 30 секунд новые видео
})
