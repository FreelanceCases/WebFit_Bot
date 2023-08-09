package retrofit

import functions.retrofit.ModelForRequest
import functions.retrofit.ResponseModel
import retrofit2.Call
import retrofit2.http.*


interface ApiInterface {
    @GET("mobileapplication")
    fun getUser(): Call<MyGet>

    @POST("mobileapplication")
    fun sendReq( @Body requestModel: RequestModel):Call<ResponseModel>

    @POST("mobile/{id}")
    fun sendParams(@Path("id") id:String,@Body modelForRequest: ModelForRequest):Call<ResponseModel>
}
