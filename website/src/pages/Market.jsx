export default function Market() {
    const products = [
        { name: "Basmati Rice", description: "Premium long-grain basmati rice known for its aromatic fragrance.", price: 10 },
        { name: "Masala Chai Blend", description: "Authentic blend of Indian spices and tea leaves for brewing traditional masala chai.", price: 15 },
        { name: "Handloom Saree", description: "Elegant handloom saree woven with intricate designs by skilled artisans.", price: 50 },
        { name: "Spice Box (Masala Dabba)", description: "Traditional Indian spice box containing essential spices for cooking flavorful meals.", price: 20 },
        { name: "Mango Pickle", description: "Homemade mango pickle made with ripe mangoes and aromatic spices.", price: 8 },
        { name: "Ayurvedic Herbal Tea", description: "Nourishing blend of Ayurvedic herbs and spices for promoting wellness and vitality.", price: 12 },
    ];
    return (
        <main className="p-10">
            <h1 className="font-bold text-2xl">Farmer's Marketplace</h1>
            <p className="text-lg mb-6">
                Integrates a marketplace platform where farmers can sell their produce at fair prices, including Minimum Support Price (MSP).
                Empowers farmers to access fair trade opportunities and increase their income.
            </p>
            <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
                {/* Render random product cards */}
                {products.map((product, index) => (
                    <div key={index} className="bg-white p-6 rounded-lg shadow-md">
                        <h2 className="text-xl font-bold mb-2">{product.name}</h2>
                        <p className="text-gray-600">{product.description}</p>
                        <div className="mt-4 flex justify-between items-center">
                            <span className="text-lg font-bold">&#8377;{product.price}</span>
                            <button className="px-4 py-2 bg-green-600 text-white rounded-md hover:bg-green-700 transition-all duration-150">Buy Now</button>
                        </div>
                    </div>
                ))}
            </div>
        </main>
    )
}