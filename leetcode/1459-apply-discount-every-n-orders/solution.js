var Cashier = function(n, discount, products, prices) {
    this.n = n;
    this.discountFactor = (100 - discount) / 100;
    this.priceMap = new Map();
    this.customerCount = 0;
    
    for (let i = 0; i < products.length; i++) {
        this.priceMap.set(products[i], prices[i]);
    }
};
Cashier.prototype.getBill = function(product, amount) {
    this.customerCount++;
    
    let subtotal = 0;
    for (let i = 0; i < product.length; i++) {
        subtotal += this.priceMap.get(product[i]) * amount[i];
    }
    
    if (this.customerCount % this.n === 0) {
        return subtotal * this.discountFactor;
    }
    
    return subtotal;
};
