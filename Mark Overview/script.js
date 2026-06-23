const Database = require("better-sqlite3");
const localDB = new Database("Mark Overview_HTML/local.db");

localDB.exec(
	"CREATE TABLE IF NOT EXISTS subjects (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, description TEXT)",
);
