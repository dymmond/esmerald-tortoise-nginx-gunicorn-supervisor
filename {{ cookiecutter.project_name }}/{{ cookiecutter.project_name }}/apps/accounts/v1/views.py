from esmerald import APIView, JSONResponse, get


class WelcomeAPIView(APIView):
    path = "/welcome"

    @get(description="Welcome home api")
    async def home(self) -> JSONResponse:
        return JSONResponse({"detail": "Welcome home!"})
