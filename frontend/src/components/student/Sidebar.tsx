import { useNavigate } from "react-router-dom";
import MainView from "./MainView";
import { useState } from "react";
const Sidebar = () => {
  const [mainViewState, setMainViewState] = useState("home");
  const navigate = useNavigate();
  return (
    <div className="drawer lg:drawer-open">
      <input id="my-drawer-2" type="checkbox" className="drawer-toggle" />
      <div className="drawer-content flex flex-col items-center ">
        <MainView state={mainViewState} />
        <label
          htmlFor="my-drawer-2"
          className="btn btn-primary drawer-button lg:hidden"
        >
          Open drawer
        </label>
      </div>
      <div className="drawer-side">
        <label
          htmlFor="my-drawer-2"
          aria-label="close sidebar"
          className="drawer-overlay"
        ></label>
        <ul className="menu bg-base-200 text-base-content min-h-full w-80 p-4">
          <li className="mb-4">
            <h1 className="font-bold text-xl">Student Dashboard</h1>
            <span className="border-b-2 h-0 border-gray-400 rounded-none" />
          </li>
          <li>
            <a onClick={() => setMainViewState("home")}>Home</a>
          </li>
          <li>
            <a onClick={() => setMainViewState("grades")}>Grades</a>
          </li>
          <li>
            <a></a>
          </li>
          <li className="mt-auto flex items-center ">
            <button
              className="btn btn-sm w-full bg-red-500 text-white"
              onClick={() => {
                localStorage.removeItem("access_token");
                navigate("/login");
              }}
            >
              Logout
            </button>
          </li>
        </ul>
      </div>
    </div>
  );
};

export default Sidebar;
