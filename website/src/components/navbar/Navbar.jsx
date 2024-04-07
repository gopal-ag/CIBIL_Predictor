import { Link } from "react-router-dom";

const Navbar = () => {

    const profileImage = "https://e7.pngegg.com/pngimages/799/987/png-clipart-computer-icons-avatar-icon-design-avatar-heroes-computer-wallpaper-thumbnail.png";

    return (
        <div className="">
            <header className="flex justify-around items-center py-5 border-b ">
                <div className="flex column items-center gap-7">
                    <h1 className="text-3xl font-bold">CropCare</h1>
                    <Link to={"/"} className="hover:underline">Dashboard</Link>
                    <Link to={"marketplace"} className="hover:underline">Marketplace</Link>
                </div>
                <div className="flex items-center gap-5">
                    <img src={profileImage} alt={"img"} className="rounded-full" width={50}/>
                    <span>Ram Gopal</span>
                </div>
            </header>
        </div>
    )
}

export default Navbar
