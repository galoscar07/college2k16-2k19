using System;
using Plugin.Connectivity;

namespace ExamREST.Utilits
{
    public static class ConnectionManager
    {
        public static bool CheckConnection()
        {
            return CrossConnectivity.Current.IsConnected;
        }
    }
}
