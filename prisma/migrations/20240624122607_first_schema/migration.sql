-- CreateTable
CREATE TABLE "ProdutoEntrada" (
    "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    "name" TEXT NOT NULL,
    "quantity" INTEGER NOT NULL,
    "entryDate" DATETIME NOT NULL,
    "employeeEntry" TEXT NOT NULL
);

-- CreateTable
CREATE TABLE "ProdutoSaida" (
    "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    "name" TEXT NOT NULL,
    "quantity" INTEGER NOT NULL,
    "leftDate" DATETIME NOT NULL,
    "customerName" TEXT NOT NULL,
    "employeeLeft" TEXT NOT NULL
);

-- CreateTable
CREATE TABLE "ProdutosTotal" (
    "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    "name" TEXT NOT NULL,
    "amount" INTEGER NOT NULL
);
