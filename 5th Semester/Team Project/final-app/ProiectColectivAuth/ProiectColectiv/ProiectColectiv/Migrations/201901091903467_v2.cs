namespace ProiectColectiv.Migrations
{
    using System;
    using System.Data.Entity.Migrations;
    
    public partial class v2 : DbMigration
    {
        public override void Up()
        {
            DropPrimaryKey("dbo.Attendances");
            AddColumn("dbo.Attendances", "id", c => c.Long(nullable: false, identity: true));
            AlterColumn("dbo.Attendances", "Type", c => c.String());
            AddPrimaryKey("dbo.Attendances", "id");
        }
        
        public override void Down()
        {
            DropPrimaryKey("dbo.Attendances");
            AlterColumn("dbo.Attendances", "Type", c => c.String(nullable: false, maxLength: 128));
            DropColumn("dbo.Attendances", "id");
            AddPrimaryKey("dbo.Attendances", new[] { "WeekNumber", "Type" });
        }
    }
}
