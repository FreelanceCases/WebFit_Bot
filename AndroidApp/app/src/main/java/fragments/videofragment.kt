package fragments

import android.net.Uri
import androidx.compose.foundation.background
import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material.Text
import androidx.compose.material.TextField
import androidx.compose.runtime.*
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.clip
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.text.style.TextAlign
import androidx.compose.ui.unit.dp
import androidx.compose.ui.viewinterop.AndroidView
import androidx.navigation.NavHostController
import com.google.android.exoplayer2.C.VIDEO_CHANGE_FRAME_RATE_STRATEGY_OFF
import com.google.android.exoplayer2.MediaItem
import com.google.android.exoplayer2.SimpleExoPlayer
import com.google.android.exoplayer2.source.ProgressiveMediaSource
import com.google.android.exoplayer2.ui.PlayerView

import com.google.android.exoplayer2.upstream.DataSource
import com.google.android.exoplayer2.upstream.DefaultDataSourceFactory
import com.google.android.exoplayer2.util.Util
import functions.retrofit.ModelForRequest
import retrofit.ModelForGet
import retrofit.postParam

@Composable
fun VideoReciever(currentStake: MutableState<ModelForGet>, navController: NavHostController) {
    var color= remember {
        mutableStateOf(0)
    }
    var button_clicked= remember {
        mutableStateOf(false)
    }
    Column(modifier = Modifier.fillMaxSize()) {
        Column(modifier = Modifier
            .fillMaxSize()
            .background(Color.Black)) {
            var text by remember { mutableStateOf("") }
            if(button_clicked.value==false){
                video_Reciever(currentStake = currentStake, button_clicked =button_clicked ,color)}
            else{
                Box_text(button_clicked,currentStake)
                TextField(
                    modifier = Modifier.padding(start = 40.dp,end=40.dp).background(Color.Black),
                    value = text,
                    onValueChange = { text = it }, placeholder = { Text(text = "Просмотренно", color = Color.White)}
                )
                Row(
                    Modifier
                        .height(350.dp)
                        .fillMaxHeight()) {Displa(button_clicked =button_clicked,color)}
            }


            Row(Modifier.padding(top=40.dp, bottom = 10.dp)){
                btn(title = "Accept", button_clicked,Color =Color.Green,ModelForRequest(text,"Accept",color.value),currentStake.value.mobile.toString(),currentStake,navController)
                btn(title = "Reject",button_clicked, Color =Color.Red,ModelForRequest(text,"Reject",color.value),currentStake.value.mobile.toString(),currentStake,navController)
            }
    }



   
    }

}



@Composable
fun btn(
    title: String,
    button_clicked:MutableState<Boolean>,
    Color:Color,
    data:ModelForRequest,
    value:String,
    currentStake: MutableState<ModelForGet>,
    navController: NavHostController
){
    Row( modifier = Modifier
        .requiredSize(width = 320.dp, height = 245.dp)
        .padding(bottom = 175.dp, end = 30.dp)
        //.clip(shape = RoundedCornerShape(40.dp))
        .fillMaxSize()
        .background(Color)
        .clickable {
            if (button_clicked.value == true) {
                postParam(value, data)
                button_clicked.value = false
                navController.navigate("videos")
            } else {
                button_clicked.value = true

            }

        }){
        Text(text = title)
    }
}

@Composable
fun list_of_colors(how_much:Int,col: MutableState<Int>){
    val colores= arrayOf(Color(255, 64, 64),Color.Red,Color(255, 116, 0),Color(255, 222, 64),Color.Green,Color.Cyan)
    for (i in 0..how_much){
    Row(modifier = Modifier
        .padding(end = 20.dp)
        .requiredSize(width = 20.dp, height = 20.dp)
        .clip(
            RoundedCornerShape(10.dp)
        )
        .background(colores[i])
        .fillMaxSize()
        .clickable { col.value = i }){}}
}

@Composable
fun video_Reciever(currentStake: MutableState<ModelForGet>, button_clicked: MutableState<Boolean>,col: MutableState<Int>){
    Column(horizontalAlignment = Alignment.CenterHorizontally, modifier = Modifier
        .padding(top = 200.dp, bottom = 400.dp)
        .requiredSize(520.dp)
        .fillMaxSize()) {
        val context = LocalContext.current
        // TODO: EDIT
        val videoUrl = "http://10.0.2.2:3000/video/${currentStake.value.mobile.toString()}"

        val exoPlayer = remember(context) {
            SimpleExoPlayer.Builder(context).setVideoChangeFrameRateStrategy(
                VIDEO_CHANGE_FRAME_RATE_STRATEGY_OFF
            ).build().apply {
                val dataSourceFactory: DataSource.Factory = DefaultDataSourceFactory(
                    context,
                    Util.getUserAgent(context, context.packageName)
                )

                val source = ProgressiveMediaSource.Factory(dataSourceFactory)
                    .createMediaSource(MediaItem.fromUri(Uri.parse(videoUrl)))

                this.prepare(source)
            }
        }

        AndroidView(factory = { context ->
            PlayerView(context).apply {
                player = exoPlayer
            }
        })
        Displa(button_clicked = button_clicked,col)
    }}

@Composable
fun Box_text(button_clicked: MutableState<Boolean>,currentStake: MutableState<ModelForGet>){
        Column(
            modifier = Modifier
                .padding(start = 5.dp, top = 100.dp, bottom = 200.dp, end = 5.dp)
                .height(200.dp)
                .fillMaxWidth()
        ) {
            Text(text = "Выберете цвет для идентификации отказа", textAlign = TextAlign.Center)
        }
}

@Composable
fun Displa(button_clicked: MutableState<Boolean>,col:MutableState<Int>){
    Row(
        modifier = Modifier
            .padding(top = 20.dp, end = 2.dp)
            .height(25.dp)
            .fillMaxWidth(), horizontalArrangement = Arrangement.Center
    ) {
        if (button_clicked.value == false) {
            list_of_colors(0,col)
        } else {
            list_of_colors( 5,col)
        }
}}


@Composable
fun UserInput(modifier: Modifier = Modifier.background(Color.White)){

}