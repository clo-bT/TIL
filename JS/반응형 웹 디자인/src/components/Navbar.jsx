import { useState } from "react";
// import React, { useState } from "react";
import styled from "styled-components";

const NavbarWrapper = styled.nav`
  display: flex;
  justify-content: space-between;
  align-items: center;
  background-color: #333;
  padding: 10px 20px;
  color: white;
`;

const Logo = styled.div`
  font-size: 24px;
  font-weight: bold;
`;

const NavLinks = styled.ul`
  display: flex;
  list-style: none;
  margin: 0;
  padding: 0;

  li {
    margin: 0 10px;

    a {
      color: white;
      text-decoration: none;
    }
  }

  @media (max-width: 768px) {
    flex-direction: column;
    background-color: #444;
    position: absolute;
    top: 60px;
    right: 0;
    width: 200px;
    padding: 10px 0;
    display: ${({ isOpen }) => (isOpen ? "flex" : "none")};
  }
`;

const MenuToggle = styled.button`
  display: none;
  background: none;
  border: none;
  color: white;
  font-size: 20px;
  cursor: pointer;

  @media (max-width: 768px) {
    display: block;
  }
`;

const Navbar = () => {
  const [menuOpen, setMenuOpen] = useState(false);

  const toggleMenu = () => {
    setMenuOpen((prev) => !prev);
  };

  return (
    <NavbarWrapper>
      <Logo href="/">Logo</Logo>
      <NavLinks isOpen={menuOpen}>
        <li>
          <a href="#">Home</a>
        </li>
        <li>
          <a href="#">About</a>
        </li>
        <li>
          <a href="#">Services</a>
        </li>
        <li>
          <a href="#">Contact</a>
        </li>
      </NavLinks>
      <MenuToggle onClick={toggleMenu}>☰</MenuToggle>
    </NavbarWrapper>
  );
};

export default Navbar;
