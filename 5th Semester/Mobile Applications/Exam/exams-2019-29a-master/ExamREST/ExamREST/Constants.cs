namespace ExamREST
{
    public static class Constants
    {
        public class Rest
        {
            public static class RestConfig
            {
                public static readonly string EncodingApplicationJson = "application/json";
                public static string Username = "Xamarin";
                public static string Password = "Pa$$w0rd";
            }

            public static class RestUrls
            {
                public static readonly string RestUrl = "https://localhost:2029/{0}";
                public static readonly string RestUrlSeparator = "/";
                public static readonly string RestUrlImportExport = "https://itec-app.herokuapp.com/personal-agenda/";
            }

            public static class RestHttpMethods
            {
                public static readonly string PatchMethod = "PATCH";
                public static readonly string GetMethod = "GET";
                public static readonly string PostMethod = "POST";
            }
        }

        public static class ResponseCodes
        {
            public static readonly string UnauthorizedErrorCode = "401";
            public static readonly string ForbiddenErrorCode = "403";
            public static readonly string NotFoundErrorCode = "404";
        }

        public static class ErrorMessages
        {
            public static readonly string GenericRequestFailedMessage = "Connection failed!";
            public static readonly string GenericInvalidActionMessage = "You are trying to perform an invalid action!";
            public static readonly string NotFoundMessage = "Specified agenda does not exist!";
            public static readonly string ExportFailedMessage = "Saving failed due to a request error!";
            public static readonly string RequestTimedOutMessage = "Request timed out! Please check your network connection.";
        }

        public static class Json
        {
            public const string IdName = "id";
        }
    }
}
