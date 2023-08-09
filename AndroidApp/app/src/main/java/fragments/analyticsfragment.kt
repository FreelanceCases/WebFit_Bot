package fragments

import android.util.Log
import androidx.compose.foundation.background
import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material.Button
import androidx.compose.material.Text
import androidx.compose.material.TextField
import androidx.compose.runtime.*
import androidx.compose.runtime.saveable.rememberSaveable
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.clip
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.text.TextStyle
import androidx.compose.ui.text.style.TextAlign
import androidx.compose.ui.unit.dp
import androidx.navigation.NavController
import androidx.navigation.NavHostController
import retrofit.ModelForGet
import retrofit.RequestModel


@Composable
fun Analytics(ValuesOfNames: MutableState<ModelForGet>,nav:NavHostController){
    val nameOfColumn= arrayOf("Google Таблица", "Диета  ", "Доступ","Тренировка")
    val valueOfColumn= arrayOf(ValuesOfNames.value.googlesheets,ValuesOfNames.value.diete,ValuesOfNames.value.approved,ValuesOfNames.value.payment)


    Box(modifier = Modifier
        .background(Color.Black)
        .fillMaxSize()) {
          Box(
              Modifier
                  .padding(
                      start = 340.dp,
                      top = 10.dp, end = 10.dp
                  )
                  .requiredSize(30.dp)
                  .clip(shape = RoundedCornerShape(50.dp))
                  .background(Color.Green)
                  .fillMaxSize()
                  .clickable {
                      retrofit.postData(
                          RequestModel(
                              ValuesOfNames.value.mobile.toString(),
                              ValuesOfNames.value.googlesheets.toString(),
                              ValuesOfNames.value.diete.toString(),
                              ValuesOfNames.value.approved.toString(),
                              ValuesOfNames.value.payment.toString()
                          )
                      )
                  }) {
          }
            Box(
                modifier = Modifier
                    .padding(top = 10.dp, start = 50.dp, end = 50.dp)
                    .height(30.dp)
                    .background(Color.Unspecified)
                    .fillMaxWidth()
            ) {
                Row(horizontalArrangement = Arrangement.Center) {
                    Text(textAlign = TextAlign.Center, modifier = Modifier.background(Color.Black), color = Color.White,text = ValuesOfNames.value.mobile.toString())
                }
            }
            Column(Modifier.padding(top = 80.dp, start = 5.dp, end = 5.dp)) {
                for (i in 0.. nameOfColumn.size-1) {

                    Row(modifier = Modifier
                        .padding(top = 25.dp)
                        .fillMaxWidth()) {
                            Text( modifier = Modifier
                                .background(Color.Black)
                                .width(70.dp),textAlign = TextAlign.Start,  text = nameOfColumn[i],color= Color.White)
                        Row(modifier = Modifier
                            .padding(start = 40.dp)
                            .fillMaxWidth(), horizontalArrangement = Arrangement.End) {
                        TextField( value = valueOfColumn[i].toString(), onValueChange = { valueOfColumn[i]=it
                            Log.e(i.toString(),valueOfColumn[i].toString())
                            ValuesOfNames.value=ValuesOfNames.value.copy(mobile = ValuesOfNames.value.mobile.toString(), googlesheets = valueOfColumn[0], diete = valueOfColumn[1],approved =valueOfColumn[2], payment = valueOfColumn[3])
                        }, textStyle = TextStyle(Color.White))
                        // Text(textAlign = TextAlign.Right, modifier = Modifier.background(Color.Black), text = ValuesOfNames[i].toString(), color = Color.White)
                        }
                        }


                    }
                Button(modifier = Modifier.fillMaxWidth(),onClick = {nav.navigate("videos")  }) {
                    Text("Click")
                }
                }
//            Column(Modifier.padding(top=380.dp,start=200.dp,end=5.dp)) {
//                for (i in ValuesOfNames){
//                    Row(modifier = Modifier.padding(top = 10.dp)) {
//                        Box(modifier = Modifier
//                            .fillMaxWidth()
//                            .background(Color.Magenta)) {
//                            Text(text = i.toString(), color = Color.Black)
//                        }}
//                }
//            }
            }

    }

fun awda(l:MutableState<Array<String>>,i:Int,newString:String): Array<String> {
    l.value.set(i,newString)
    return l.value.clone()
}