package com.softify.webfitness

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import fragments.FirstScreen
import fragments.Nav
import retrofit.getMyData


class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContent {
            Nav()
            //Analytics()
            //VideoReciever()
                }
     }
    }

