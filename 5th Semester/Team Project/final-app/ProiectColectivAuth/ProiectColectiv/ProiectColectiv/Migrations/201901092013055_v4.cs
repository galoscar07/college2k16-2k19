namespace ProiectColectiv.Migrations
{
    using System;
    using System.Data.Entity.Migrations;
    
    public partial class v4 : DbMigration
    {
        public override void Up()
        {
            AddColumn("dbo.Attendances", "TypeOf", c => c.String());
            DropColumn("dbo.Attendances", "Type");
        }
        
        public override void Down()
        {
            AddColumn("dbo.Attendances", "Type", c => c.String());
            DropColumn("dbo.Attendances", "TypeOf");
        }
    }
}
