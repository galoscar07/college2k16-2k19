using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Net.Http;
using System.Net.Http.Headers;
using System.Text;
using System.Threading.Tasks;
using Newtonsoft.Json;

namespace ExamREST
{
	public class RestService : IRestService
	{
		HttpClient client;

		public List<ExamItem> Items { get; private set; }

		public RestService ()
		{
			var authData = string.Format("{0}:{1}", Constants.Rest.RestConfig.Username, Constants.Rest.RestConfig.Password);
			var authHeaderValue = Convert.ToBase64String(Encoding.UTF8.GetBytes(authData));

            client = new HttpClient() { Timeout = TimeSpan.FromSeconds(5) };
            client.MaxResponseContentBufferSize = 256000;
            //client.DefaultRequestHeaders.Authorization = new AuthenticationHeaderValue("Basic", authHeaderValue);
		}

        public async Task<List<ExamItem>> GetAllTasks(){
            Items = new List<ExamItem>();
            var uri = new Uri(string.Format(Constants.Rest.RestUrls.RestUrl, "allPlaces"));
            try {
                var response = await client.GetAsync(uri);
                if (response.IsSuccessStatusCode)
                {
                    var content = await response.Content.ReadAsStringAsync();
                    Items = JsonConvert.DeserializeObject<List<ExamItem>>(content);
                }
            } catch (Exception ex)
            {
                Debug.WriteLine(@"              ERROR {0}", ex.Message);
            }

            return Items;
        }

        public async Task<List<ExamItem>> RefreshDataAsync ()
		{
			Items = new List<ExamItem> ();

			// RestUrl = http://developer.xamarin.com:8081/api/todoitems
			var uri = new Uri (string.Format (Constants.Rest.RestUrls.RestUrl, "places"));

			try {
				var response = await client.GetAsync (uri);
				if (response.IsSuccessStatusCode) {
					var content = await response.Content.ReadAsStringAsync ();
					Items = JsonConvert.DeserializeObject <List<ExamItem>> (content);
				}
			} catch (Exception ex) {
				Debug.WriteLine (@"				ERROR {0}", ex.Message);
			}

			return Items;
		}

        public async Task LoanSlotAsync(int id)
        {
            var uri = new Uri(string.Format(Constants.Rest.RestUrls.RestUrl, "take"));

            try
            {
                var sent_id = new Dictionary<string, int>() { { "id", id } };
                var json = JsonConvert.SerializeObject(sent_id);
                var content = new StringContent(json, Encoding.UTF8, "application/json");

                HttpResponseMessage response = null;
                response = await client.PostAsync(uri, content);

                if (response.IsSuccessStatusCode)
                {
                    Debug.WriteLine(@"              ExamItem successfully loaned.");
                }
            }
            catch (Exception ex)
            {
                Debug.WriteLine(@"              ERROR {0}", ex.Message);
            }
        }

        public async Task ReturnSlotAsync(int id)
        {
            var uri = new Uri(string.Format(Constants.Rest.RestUrls.RestUrl, "free"));

            try
            {
                var sent_id = new Dictionary<string, int>() { { "id", id } };
                var json = JsonConvert.SerializeObject(sent_id);
                var content = new StringContent(json, Encoding.UTF8, "application/json");

                HttpResponseMessage response = null;
                response = await client.PostAsync(uri, content);

                if (response.IsSuccessStatusCode)
                {
                    Debug.WriteLine(@"              ExamItem successfully returned.");
                }
            }
            catch (Exception ex)
            {
                Debug.WriteLine(@"              ERROR {0}", ex.Message);
            }
        }

        public async Task SaveExamItemAsync (ExamItem item, bool isNewItem = false)
		{
			// RestUrl = http://developer.xamarin.com:8081/api/todoitems
			var uri = new Uri (string.Format (Constants.Rest.RestUrls.RestUrl, string.Empty));

			try {
				var json = JsonConvert.SerializeObject (item);
				var content = new StringContent (json, Encoding.UTF8, "application/json");

				HttpResponseMessage response = null;
				if (isNewItem) {
					response = await client.PostAsync (uri, content);
				} else {
					response = await client.PutAsync (uri, content);
				}
				
				if (response.IsSuccessStatusCode) {
					Debug.WriteLine (@"				ExamItem successfully saved.");
				}
				
			} catch (Exception ex) {
				Debug.WriteLine (@"				ERROR {0}", ex.Message);
			}
		}

		public async Task DeleteExamItemAsync (int id)
		{
			// RestUrl = http://developer.xamarin.com:8081/api/todoitems/{0}
			var uri = new Uri (string.Format (Constants.Rest.RestUrls.RestUrl, "place"));

			try {

                var sent_id = new Dictionary<string, int>() { { "id", id } };
                var json = JsonConvert.SerializeObject(sent_id);
                HttpRequestMessage request = new HttpRequestMessage
                {
                    Content = new StringContent(json, Encoding.UTF8, "application/json"),
                    Method = HttpMethod.Delete,
                    RequestUri = uri
                };
                var response = await client.SendAsync(request);

				if (response.IsSuccessStatusCode) {
					Debug.WriteLine (@"				ExamItem successfully deleted.");	
				}
				
			} catch (Exception ex) {
				Debug.WriteLine (@"				ERROR {0}", ex.Message);
			}
		}
	}
}
