import React from 'react';
import './NavBar.scss'
import {Link} from "react-router-dom";

const NavBar = () => {
    return (
        <div className="navbar">
            <ul className="topnav">
                <li><Link to="/">Главная <i className="pi pi-home"></i> </Link></li>
                <li><Link to="/events">Мероприятия <i className="pi pi-calendar"></i></Link></li>
                {/*<li><Link to="/articles">Статьи <i className="pi pi-file"></i></Link></li>*/}
                {/*<li className="right"><a href="#about">About</a></li>*/}
            </ul>
        </div>
    );
};

export default NavBar;

