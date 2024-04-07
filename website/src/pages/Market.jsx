import React, { useState } from 'react';
import tea from "../assets/tea.jpeg";
import spice from "../assets/spice.jpeg";
import rice from "../assets/rice.jpeg";
import saree from "../assets/saree.jpeg";
import pickle from "../assets/pickle.jpeg";
import chai from "../assets/chai.jpeg";
import LineComp from '../components/line';
import { dataLine1 } from '../constants';

export default function Market() {
    const [modalInfo, setModalInfo] = useState(null);
    const [profits, setProfits] = useState({});

    const products = [
        { name: "Basmati Rice", description: "Premium long-grain basmati rice known for its aromatic fragrance.", price: 10, photo: rice },
        { name: "Masala Chai Blend", description: "Authentic blend of Indian spices and tea leaves for brewing traditional masala chai.", price: 15, photo: chai },
        { name: "Handloom Saree", description: "Elegant handloom saree woven with intricate designs by skilled artisans.", price: 50, photo: saree },
        { name: "Spice Box (Masala Dabba)", description: "Traditional Indian spice box containing essential spices for cooking flavorful meals.", price: 20, photo: spice },
        { name: "Mango Pickle", description: "Homemade mango pickle made with ripe mangoes and aromatic spices.", price: 8, photo: pickle },
        { name: "Ayurvedic Herbal Tea", description: "Nourishing blend of Ayurvedic herbs and spices for promoting wellness and vitality.", price: 12, photo: tea },
    ];

    const suggestedPrice = (price) => {
        return Math.floor(price * 1.2); // Suggested price is 20% higher than original price
    };

    const generateRandomProfit = () => {
        const randomProfits = {};
        products.forEach(product => {
            randomProfits[product.name] = Math.floor(Math.random() * 20) - 10; // Random profit between -10 and 10
        });
        return randomProfits;
    };

    const handleSellNow = (productName, productPrice) => {
        const suggested = suggestedPrice(productPrice);
        const profit = suggested - productPrice;
        setModalInfo({ productName, suggested, profit });
        setProfits({ ...profits, [productName]: profit });
    };

    // Generate random profits initially
    useState(() => {
        setProfits(generateRandomProfit());
    }, []);

    return (
        <main className="p-10">
            <h1 className="font-bold text-2xl mb-4">Farmer's Marketplace</h1>
            <div className="flex justify-between mb-4">
                <button className="px-4 py-2 bg-blue-600 text-white rounded-md hover:bg-blue-700 transition-all duration-150">Buy Now</button>
                <button className="px-4 py-2 bg-blue-600 text-white rounded-md hover:bg-blue-700 transition-all duration-150">Rent Now</button>
            </div>
            <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
                {/* Render random product cards */}
                {products.map((product, index) => (
                    <div key={index} className="bg-white p-6 rounded-lg shadow-md">
                        <h2 className="text-xl font-bold mb-2">{product.name}</h2>
                        <img src={product.photo} alt={product.name} className="w-full h-32 object-cover mb-4" />
                        <p className="text-gray-600">{product.description}</p>
                        <div className="mt-4 flex justify-between items-center">
                            <span className={`text-lg font-bold ${profits[product.name] !== undefined && profits[product.name] >= 0 ? 'text-green-600' : 'text-red-600'}`}>&#8377;{product.price}</span>
                            <button className="px-4 py-2 bg-green-600 text-white rounded-md hover:bg-green-700 transition-all duration-150" onClick={() => handleSellNow(product.name, product.price)}>Sell Now</button>
                        </div>
                    </div>
                ))}
            </div>

            {/* Modal */}
            {modalInfo && (
                <div className="fixed inset-0 z-10 flex items-center justify-center bg-gray-800 bg-opacity-50">
                    <div className="bg-white p-8 rounded-md">
                        {modalInfo.profit >= 0 ?
                            <p className="text-lg font-bold mb-4">You can sell {modalInfo.productName} at a profit of &#8377;{modalInfo.profit} (Suggested Price: &#8377;{modalInfo.suggested})</p> :
                            <p className="text-lg font-bold mb-4">You may incur a loss of &#8377;{Math.abs(modalInfo.profit)} if you sell {modalInfo.productName} (Suggested Price: &#8377;{modalInfo.suggested})</p>
                        }

                        {/* Dummy line graph */}
                        <LineComp data={dataLine1} />

                        <button className="px-4 py-2 bg-green-600 text-white rounded-md hover:bg-green-700 transition-all duration-150" onClick={() => setModalInfo(null)}>Close</button>
                    </div>
                </div>
            )}
        </main>
    )
}
