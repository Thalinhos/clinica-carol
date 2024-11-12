/*
  Warnings:

  - Added the required column `motivo` to the `ProdutoSaida` table without a default value. This is not possible if the table is not empty.

*/
-- RedefineTables
PRAGMA foreign_keys=OFF;
CREATE TABLE "new_ProdutoSaida" (
    "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    "name" TEXT NOT NULL,
    "quantity" INTEGER NOT NULL,
    "leftDate" TEXT NOT NULL,
    "employeeLeft" TEXT NOT NULL,
    "motivo" TEXT NOT NULL,
    "notaDeSaidaId" INTEGER,
    CONSTRAINT "ProdutoSaida_notaDeSaidaId_fkey" FOREIGN KEY ("notaDeSaidaId") REFERENCES "NotaDeSaida" ("id") ON DELETE SET NULL ON UPDATE CASCADE
);
INSERT INTO "new_ProdutoSaida" ("employeeLeft", "id", "leftDate", "name", "notaDeSaidaId", "quantity") SELECT "employeeLeft", "id", "leftDate", "name", "notaDeSaidaId", "quantity" FROM "ProdutoSaida";
DROP TABLE "ProdutoSaida";
ALTER TABLE "new_ProdutoSaida" RENAME TO "ProdutoSaida";
PRAGMA foreign_key_check;
PRAGMA foreign_keys=ON;
