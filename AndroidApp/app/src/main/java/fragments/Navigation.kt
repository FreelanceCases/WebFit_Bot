package fragments

import androidx.compose.runtime.Composable
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.navigation.compose.NavHost
import androidx.navigation.compose.composable
import androidx.navigation.compose.rememberNavController
import retrofit.ModelForGet

@Composable
fun Nav(){
    val currentStake=remember{
        mutableStateOf(ModelForGet("","","","",""))
    }
    val navController = rememberNavController()

    NavHost(navController = navController, startDestination = "firstscreen") {
        composable("firstscreen"){
            FirstScreen(navController,currentStake) }

        composable("analytics") {
            Analytics(ValuesOfNames =currentStake,navController)
        }
        composable("videos") { VideoReciever(currentStake,navController) }
    }}
