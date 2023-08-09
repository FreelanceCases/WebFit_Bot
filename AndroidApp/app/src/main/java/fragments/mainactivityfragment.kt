package fragments

import android.os.Parcel
import android.os.Parcelable
import android.util.Log
import androidx.compose.foundation.background
import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.rememberScrollState
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.foundation.verticalScroll
import androidx.compose.material.Card
import androidx.compose.material.Text
import androidx.compose.runtime.*
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.unit.dp
import androidx.navigation.NavHostController
import com.google.gson.Gson
import retrofit.ModelForGet
import retrofit.MyGet


@Composable
fun FirstScreen(OnAnalytics: NavHostController,currentStake:MutableState<ModelForGet>){
    Box(modifier = Modifier
        .background(color = Color.Black)
        .fillMaxSize()){

        Column( verticalArrangement = Arrangement.Center, horizontalAlignment = Alignment.CenterHorizontally, modifier = Modifier
            .padding(top = 80.dp)
            .verticalScroll(
                rememberScrollState()
            )) {thi(OnAnalytics,currentStake)
        }
    }
}



@Composable
fun thi(OnAnalytics: NavHostController,currentStake:MutableState<ModelForGet>){
    Log.e("MainScreen","WADA")
    val JSONwithInfo:MutableState<MyGet> = remember {
        mutableStateOf(MyGet())
    }
    retrofit.getMyData(JSONwithInfo)
    val t=JSONwithInfo.value
    for (i in t){
        var c:Color=Color.Red
        if (i.approved=="yes"){c=Color.Green}
        var k:MutableState<String?> = remember {
            mutableStateOf(i.mobile)
        }


    Card(shape = RoundedCornerShape(15.dp), modifier = Modifier
        .padding(start = 20.dp, end = 70.dp, top = 25.dp)
        .fillMaxWidth()
        .height(60.dp)
        .background(
            c
        ), elevation = 50.dp) {


        Row(verticalAlignment = Alignment.CenterVertically, horizontalArrangement = Arrangement.Center, modifier = Modifier
            .clickable(onClick =
            {currentStake.value=i
                OnAnalytics.navigate("Analytics") }
            )
            .background(Color.Black)){
            displayText(f = k)
            }
        }
    }}

//ModelForGet(i.mobile.toString(),i.googlesheets.toString(),i.diete.toString(),i.approved.toString(),i.payment.toString()

@Composable
fun displayText(f:MutableState<String?>){
    Text(text = f.value?:"No",Modifier.background(Color.Black), color = Color.White)
}