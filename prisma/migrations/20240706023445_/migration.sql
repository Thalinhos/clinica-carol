/*
  Warnings:

  - You are about to drop the `NotaDeSaida` table. If the table is not empty, all the data it contains will be lost.
  - You are about to drop the column `notaDeSaidaId` on the `ProdutoSaida` table. All the data in the column will be lost.

*/
-- DropTable
PRAGMA foreign_keys=off;
DROP TABLE "NotaDeSaida";
PRAGMA foreign_keys=on;

-- RedefineTables
PRAGMA foreign_keys=OFF;
CREATE TABLE "new_ProdutoSaida" (
    "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    "name" TEXT NOT NULL,
    "quantity" INTEGER NOT NULL,
    "leftDate" TEXT NOT NULL,
    "employeeLeft" TEXT NOT NULL,
    "motivo" TEXT NOT NULL
);
INSERT INTO "new_ProdutoSaida" ("employeeLeft", "id", "leftDate", "motivo", "name", "quantity") SELECT "employeeLeft", "id", "leftDate", "motivo", "name", "quantity" FROM "ProdutoSaida";
DROP TABLE "ProdutoSaida";
ALTER TABLE "new_ProdutoSaida" RENAME TO "ProdutoSaida";
PRAGMA foreign_key_check;
PRAGMA foreign_keys=ON;
