-- CreateTable
CREATE TABLE "NotaDeSaida" (
    "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT
);

-- RedefineTables
PRAGMA foreign_keys=OFF;
CREATE TABLE "new_ProdutoSaida" (
    "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    "name" TEXT NOT NULL,
    "quantity" INTEGER NOT NULL,
    "leftDate" TEXT NOT NULL,
    "employeeLeft" TEXT NOT NULL,
    "notaDeSaidaId" INTEGER,
    CONSTRAINT "ProdutoSaida_notaDeSaidaId_fkey" FOREIGN KEY ("notaDeSaidaId") REFERENCES "NotaDeSaida" ("id") ON DELETE SET NULL ON UPDATE CASCADE
);
INSERT INTO "new_ProdutoSaida" ("employeeLeft", "id", "leftDate", "name", "quantity") SELECT "employeeLeft", "id", "leftDate", "name", "quantity" FROM "ProdutoSaida";
DROP TABLE "ProdutoSaida";
ALTER TABLE "new_ProdutoSaida" RENAME TO "ProdutoSaida";
PRAGMA foreign_key_check;
PRAGMA foreign_keys=ON;
