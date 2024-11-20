import GradeChart from "../../common/GradeCharts";
import StudentProfile from "./StudentProfile";
interface MainViewType {
  state: string;
}
const MainView = ({ state }: MainViewType) => {
  if (state == "home") {
    return <StudentProfile />;
  } else if (state == "grades") {
    return <GradeChart />;
  } else {
    return <h1>404</h1>;
  }
};

export default MainView;
