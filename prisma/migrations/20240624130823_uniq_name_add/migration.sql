/*
  Warnings:

  - A unique constraint covering the columns `[name]` on the table `ProdutoEntrada` will be added. If there are existing duplicate values, this will fail.
  - A unique constraint covering the columns `[name]` on the table `ProdutoSaida` will be added. If there are existing duplicate values, this will fail.
  - A unique constraint covering the columns `[name]` on the table `ProdutosTotal` will be added. If there are existing duplicate values, this will fail.

*/
-- CreateIndex
CREATE UNIQUE INDEX "ProdutoEntrada_name_key" ON "ProdutoEntrada"("name");

-- CreateIndex
CREATE UNIQUE INDEX "ProdutoSaida_name_key" ON "ProdutoSaida"("name");

-- CreateIndex
CREATE UNIQUE INDEX "ProdutosTotal_name_key" ON "ProdutosTotal"("name");
