using System;
using System.Configuration;
using System.Data;
using System.Data.SqlClient;
using System.Windows.Forms;

namespace Lab1
{
    public partial class Form1 : Form
    {
        private SqlDataAdapter dataAdapter2;
        private DataSet dataSet;
        private SqlConnection connection;
        private string _serverAddr;
        private string _formTitle;
        private string _initial;
        private string _username;
        private string _password;
        private string _tableOne;
        private string _tableTwo;
        private string _columnOne;
        private string _columnTwo;
        private string _label1Text;
        private string _label2Text;

        public Form1()
        {
            InitializeComponent();

            _serverAddr = ConfigurationManager.AppSettings["ServerAddress"];
            _formTitle = ConfigurationManager.AppSettings["FormTitle"];
            _initial = ConfigurationManager.AppSettings["Initial"];
            _username = ConfigurationManager.AppSettings["UserName"];
            _password = ConfigurationManager.AppSettings["Password"];
            _tableOne = ConfigurationManager.AppSettings["TableOne"];
            _tableTwo = ConfigurationManager.AppSettings["TableTwo"];
            _columnOne = ConfigurationManager.AppSettings["ColumnForTableOne"];
            _columnTwo = ConfigurationManager.AppSettings["ColumnForTableTwo"];
            _label1Text = ConfigurationManager.AppSettings["LabelOne"];
            _label2Text = ConfigurationManager.AppSettings["LabelTwo"];

            FillData();
        }

        private void InitializeComponent()
        {
            throw new NotImplementedException();
        }

        private void FillData()
        {
            try
            {
                String connectionString =
                    "Server= " + _serverAddr + "; Initial Catalog = " + _initial + "; User ID=" + _username + "; Password=" + _password;
                connection = new SqlConnection(connectionString);
                dataSet = new DataSet();
                SqlDataAdapter dataAdapter1 = new SqlDataAdapter("SELECT TOP(100) * FROM " + _tableOne, connection);
                dataAdapter2 = new SqlDataAdapter("SELECT TOP(100) * FROM " + _tableTwo, connection);
                SqlCommandBuilder sqlCommandBuilder = new SqlCommandBuilder(dataAdapter2);
                dataAdapter1.Fill(dataSet, _tableOne);
                dataAdapter2.Fill(dataSet, _tableTwo);
                DataRelation dataRelation = new DataRelation("FK_Clients_Rents", dataSet.Tables[_tableOne].Columns[_columnOne],
                                                             dataSet.Tables[_tableTwo].Columns[_columnTwo]);
                dataSet.Relations.Add(dataRelation);
                BindingSource bs1 = new BindingSource();
                BindingSource bs2 = new BindingSource();
                bs1.DataSource = dataSet;
                bs1.DataMember = _tableOne;
                bs2.DataSource = bs1;
                bs2.DataMember = "FK_Clients_Rents";
                dataGridView1.DataSource = bs1;
                dataGridView2.DataSource = bs2;
                this.label1.Text = _label1Text;
                this.label2.Text = _label2Text;
                this.Text = _formTitle;

            }
            catch (SqlException)
            {
                MessageBox.Show("Error");
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            dataAdapter2.Update(dataSet, _tableTwo);

        }
    }
}