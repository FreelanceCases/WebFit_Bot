package retrofit

import android.annotation.SuppressLint
import android.util.Log
import androidx.compose.runtime.MutableState
import functions.retrofit.ModelForRequest
import functions.retrofit.ResponseModel
import retrofit2.Call
import retrofit2.Callback
import retrofit2.Retrofit
import retrofit2.Response
import retrofit2.converter.gson.GsonConverterFactory

fun retrofitBuilder(): ApiInterface {
//    var BaseUrl="http://134.0.118.41:3000/"
    // TODO: Edit
//    var BaseUrl="http://127.0.0.1:3000/"
    var BaseUrl="http://10.0.2.2:3000/"
    val retrofitBuilder by lazy { Retrofit.Builder().baseUrl(BaseUrl).addConverterFactory(GsonConverterFactory.create()).build().create(ApiInterface::class.java)}
     return retrofitBuilder
}

     fun getMyData(data: MutableState<MyGet>){
        val retrofitData = retrofitBuilder().getUser()
        retrofitData.enqueue(object : Callback<MyGet> {
            override fun onResponse(
                call: Call<MyGet?>,
                response: Response<MyGet?>
            ){
                data.value=response.body()!!
            }

            override fun onFailure(call: Call<MyGet?>, t: Throwable) {
                Log.e("ERR",t.toString())
            }
        }
        )

    }

    @SuppressLint("SuspiciousIndentation")
    fun postData(Data:RequestModel){
       val RB=retrofitBuilder().sendReq(requestModel = Data)
           RB.enqueue(
            object : Callback<ResponseModel> {
                override fun onResponse(
                    call: Call<ResponseModel>,
                    response: Response<ResponseModel>
                ) {
                    Log.e("ERR","DAWDAWD")

                }

                override fun onFailure(call: Call<ResponseModel>, t: Throwable) {
                   Log.e("ERR",t.toString())
                }
            })
    }

  fun postParam(mobile:String,Par:ModelForRequest){
      val RB=retrofitBuilder().sendParams(mobile,Par)
      RB.enqueue(
          object : Callback<ResponseModel> {
              override fun onResponse(
                  call: Call<ResponseModel>,
                  response: Response<ResponseModel>
              ) {
                  Log.e("Sended","Yep")

              }

              override fun onFailure(call: Call<ResponseModel>, t: Throwable) {
                  Log.e("ERR",t.toString())
              }
          })

  }





