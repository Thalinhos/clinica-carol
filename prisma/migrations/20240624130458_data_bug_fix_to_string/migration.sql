-- RedefineTables
PRAGMA foreign_keys=OFF;
CREATE TABLE "new_ProdutoSaida" (
    "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    "name" TEXT NOT NULL,
    "quantity" INTEGER NOT NULL,
    "leftDate" TEXT NOT NULL,
    "customerName" TEXT NOT NULL,
    "employeeLeft" TEXT NOT NULL
);
INSERT INTO "new_ProdutoSaida" ("customerName", "employeeLeft", "id", "leftDate", "name", "quantity") SELECT "customerName", "employeeLeft", "id", "leftDate", "name", "quantity" FROM "ProdutoSaida";
DROP TABLE "ProdutoSaida";
ALTER TABLE "new_ProdutoSaida" RENAME TO "ProdutoSaida";
CREATE TABLE "new_ProdutoEntrada" (
    "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    "name" TEXT NOT NULL,
    "quantity" INTEGER NOT NULL,
    "entryDate" TEXT NOT NULL,
    "employeeEntry" TEXT NOT NULL
);
INSERT INTO "new_ProdutoEntrada" ("employeeEntry", "entryDate", "id", "name", "quantity") SELECT "employeeEntry", "entryDate", "id", "name", "quantity" FROM "ProdutoEntrada";
DROP TABLE "ProdutoEntrada";
ALTER TABLE "new_ProdutoEntrada" RENAME TO "ProdutoEntrada";
PRAGMA foreign_key_check;
PRAGMA foreign_keys=ON;
