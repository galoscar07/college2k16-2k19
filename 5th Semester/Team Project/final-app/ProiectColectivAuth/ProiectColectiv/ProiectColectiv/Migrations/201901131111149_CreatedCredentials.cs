namespace ProiectColectiv.Migrations
{
    using System;
    using System.Data.Entity.Migrations;
    
    public partial class CreatedCredentials : DbMigration
    {
        public override void Up()
        {
            CreateTable(
                "dbo.Credentials",
                c => new
                    {
                        Email = c.String(nullable: false, maxLength: 128),
                        Password = c.String(),
                        Role = c.String(),
                    })
                .PrimaryKey(t => t.Email);
            
        }
        
        public override void Down()
        {
            DropTable("dbo.Credentials");
        }
    }
}
