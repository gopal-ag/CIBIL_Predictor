import LineComp from "../components/line";
import PieComp from "../components/pie/pie";
import { dataLine1, dataLine2, dataPie1, dataPie2, dataPie3, dataPie4 } from "../constants";
import sunny from "../assets/sunny.png"

export default function Home() {
    return (
        <main className="p-10">
            <div className="flex">
                <div className="flex flex-col  w-3/4">
                    <div className="flex">
                        <div className="flex m-5 border border-gray-300 rounded-xl w-2/3 max-h-64 shadow-md">
                            <PieComp data={dataPie1} />
                            <PieComp data={dataPie2} />
                            <PieComp data={dataPie3} />
                            <PieComp data={dataPie4} />
                        </div>
                        <div className="m-5 border w-1/3 rounded-xl p-5 shadow-md flex flex-col items-center">
                            <h1 className="text-xl font-bold ">Climate</h1>
                            <img src={sunny} alt="" width={150} />
                        </div>
                    </div>
                    <div className="flex">
                        <div className="border m-10 flex flex-col gap-7 p-10 rounded-xl w-1/3 shadow-md">
                            <h1 className="font-bold text-2xl">Perfection: <span className="text-green-600">76%</span></h1>
                            <p className="text-medium">Fertilizer A: <span className="text-green-600">89%</span></p>
                            <p className="text-medium">Fertilizer B: <span className="text-green-600">56%</span></p>
                        </div>
                        <div className="w-2/3 m-10 border rounded-xl p-10 shadow-md">
                            <h1 className="text-xl font-bold">Predictions</h1>
                            Based on soil contents, predictions for agriculture include favorable conditions for crops like corn in nitrogen-rich soils, blueberries in acidic pH levels, beans in phosphorus-rich soils, potatoes in potassium-rich soils, and consideration of salinity for crop selection, such as avoiding spinach in high-salinity areas.
                        </div>
                    </div>
                </div>
                <div className="w-1/4 border shadow-md border-gray-300 h-[60vh] m-5 gap-3 flex flex-col rounded-xl">
                    <h1 className="font-bold px-4 py-4">Cost prize:</h1>
                    <h1 className="font-bold px-4">Predected Market Cost:</h1>
                    <h1 className="font-bold px-4">Min selling Cost (for profit):</h1>

                    <LineComp data={dataLine1} />
                </div>
            </div>


            <hr />

            <div className="flex">
                <div className="w-2/3 m-10 border-2 p-5 rounded-xl">
                    <h1 className="font-bold text-xl">Past Credit Score</h1>
                    <LineComp data={dataLine2} />
                </div>
                <div className="w-1/3 m-10 border-2 rounded-xl p-5">
                    <h1 className="text-xl font-bold">Ways To Get Better Score:</h1>
                    <li className="flex flex-col gap-3">
                        <li>Lorem ipsum dolor sit amet.</li>
                        <li>Lorem ipsum dolor sit amet.</li>
                        <li>Lorem ipsum dolor sit amet.</li>
                    </li>
                </div>
            </div>

        </main>
    )
}