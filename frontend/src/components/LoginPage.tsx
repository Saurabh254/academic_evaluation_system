import { useState } from "react";
import { HandleUserLogin } from "../services/auth";
import { useNavigate } from "react-router-dom";

const LoginPage = () => {
  const [type, setType] = useState("student");
  const navigate = useNavigate();
  const [formData, SetFormData] = useState({
    identity: "",
    password: "",
  });
  return (
    <div className="bg-base-200 min-h-screen flex items-center justify-center">
      <div className="card lg:card-side bg-base-100 shadow-xl max-w-4xl w-full">
        <figure className="lg:w-1/2">
          <img
            src="/academic_system_logo.png"
            alt="Random image"
            className="object-cover w-full h-full"
          />
        </figure>
        <div className="card-body lg:w-1/2 flex items-center justify-center">
          <h2 className="card-title text-2xl font-bold mb-6 flex w-full text-center items-center justify-center">
            {type == "student" ? "Student Login" : "Teacher Login"}
          </h2>
          <form>
            <div className="form-control">
              <label className="label">
                <span className="label-text">
                  {type == "student" ? "Enrollment No." : "Registration No."}
                </span>
              </label>
              <label className="input input-bordered flex items-center gap-2">
                <span className="ri-user-line"></span>
                <input
                  type="email"
                  className="grow"
                  placeholder={type == "student" ? "0115CS00000" : "TEC1452827"}
                  value={formData.identity}
                  onChange={(e) => {
                    SetFormData({ ...formData, identity: e.target.value });
                  }}
                  required
                />
              </label>
            </div>
            <div className="form-control mt-4">
              <label className="label">
                <span className="label-text">Password</span>
              </label>
              <label className="input input-bordered flex items-center gap-2">
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  viewBox="0 0 16 16"
                  fill="currentColor"
                  className="w-4 h-4 opacity-70"
                >
                  <path
                    fillRule="evenodd"
                    d="M14 6a4 4 0 0 1-4.899 3.899l-1.955 1.955a.5.5 0 0 1-.353.146H5v1.5a.5.5 0 0 1-.5.5h-2a.5.5 0 0 1-.5-.5v-2.293a.5.5 0 0 1 .146-.353l3.955-3.955A4 4 0 1 1 14 6Zm-4-2a.75.75 0 0 0 0 1.5.5.5 0 0 1 .5.5.75.75 0 0 0 1.5 0 2 2 0 0 0-2-2Z"
                    clipRule="evenodd"
                  />
                </svg>
                <input
                  type="password"
                  className="grow"
                  placeholder="Enter password"
                  value={formData.password}
                  onChange={(e) => {
                    SetFormData({ ...formData, password: e.target.value });
                  }}
                  required
                />
              </label>
              <label className="label">
                <a href="#" className="label-text-alt link link-hover">
                  Forgot password?
                </a>
              </label>
            </div>
            <div className="form-control mt-6">
              <button
                className="btn btn-primary"
                onClick={() => {
                  HandleUserLogin(formData)
                    .then((response) => {
                      navigate("/");
                      if (response.status == 200) {
                        navigate("/");
                      }
                    })
                    .catch((e) => alert(e));
                }}
              >
                Login
              </button>
            </div>
          </form>
          <div className="divider">OR</div>
          <div className="text-center">
            <button
              onClick={() => {
                setType(type == "student" ? "teacher" : "student");
                SetFormData({ identity: "", password: "" });
              }}
              className="link link-primary"
            >
              Login as Teacher
            </button>
          </div>
        </div>
      </div>
    </div>
  );
};

export default LoginPage;
