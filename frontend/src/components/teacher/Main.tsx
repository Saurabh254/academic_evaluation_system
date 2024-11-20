import { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import MainView from "./MainView";

const Main = () => {
  const navigate = useNavigate();

  return (
    <div className="drawer lg:drawer-open">
      <input id="my-drawer-2" type="checkbox" className="drawer-toggle" />
      <div className="drawer-content flex flex-col items-center ">
        <MainView />
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
            <h1 className="font-bold text-xl">Teacher Dashboard</h1>
            <span className="border-b-2 h-0 border-gray-400 rounded-none" />
          </li>
          <li>
            <Link to=""> Home</Link>
          </li>
          <li>
            <Link to="students"> Students list </Link>
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

export default Main;