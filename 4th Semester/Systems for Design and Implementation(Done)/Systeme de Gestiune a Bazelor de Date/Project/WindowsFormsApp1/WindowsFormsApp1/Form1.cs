using System;
using System.Data;
using System.Data.SqlClient;
using System.Windows.Forms;

namespace WindowsFormsApp1
{
    public partial class Form1 : Form
    {
        private BindingSource bindingSource1 = new BindingSource();
        private SqlDataAdapter dataAdapter = new SqlDataAdapter();

        public Form1()
        {
            InitializeComponent();
            FillData();
        }

        private void FillData()
        {
            try
            {
                String connectionString = "Data Source= DESKTOP-M6SNDNU; Initial Catalog = MovieRentalShop; Integrated Security=true";
                dataAdapter = new SqlDataAdapter("SELECT * FROM Customers", connectionString);
                DataTable table = new DataTable();
                dataAdapter.Fill(table);
                bindingSource1.DataSource = table;
                dataGridView1.DataSource = bindingSource1;
                DataColumn parentColumn parentColumn = DataSet1.Tables["Customers"].Columns["id"];
              

                /*private void CreateRelation()
                {   // Get some help :* 
                    // Get the DataColumn objects from two DataTable objects 
                    // in a DataSet. Code to get the DataSet not shown here.
                    DataColumn parentColumn =
                        DataSet1.Tables["Customers"].Columns["CustID"];
                    DataColumn childColumn =
                        DataSet1.Tables["Orders"].Columns["CustID"];
                    // Create DataRelation.
                    DataRelation relCustOrder;
                    relCustOrder = new DataRelation("CustomersOrders",
                        parentColumn, childColumn);
                    // Add the relation to the DataSet.
                    DataSet1.Relations.Add(relCustOrder);
                }*/
            }
            catch (SqlException)
            {
                MessageBox.Show("Error");
            }
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void dataGridView1_CellContentClick(object sender, DataGridViewCellEventArgs e)
        {

        }
    }
}
