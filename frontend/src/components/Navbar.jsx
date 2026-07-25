import "../styles/Navbar.css";

function Navbar() {

  const today = new Date();

  return (

    <div className="navbar">

      <div>

        <h2>TeamSync Dashboard</h2>

        <p>
          {today.toDateString()}
        </p>

      </div>

      <div className="profile">

        <div className="avatar">
          A
        </div>

        <span>Admin</span>

      </div>

    </div>

  );

}

export default Navbar;