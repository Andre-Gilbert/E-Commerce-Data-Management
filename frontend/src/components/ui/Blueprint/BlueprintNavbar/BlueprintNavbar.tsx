/** The navbar of the data management application. */
import {
  Navbar,
  NavbarGroup,
  NavbarHeading,
  Button,
  Classes,
} from '@blueprintjs/core';

export const BlueprintNavbar = () => {
  return (
    <Navbar>
      <NavbarGroup>
        <NavbarHeading>404</NavbarHeading>
        <Button className={Classes.MINIMAL} icon="home" text="Home" />
        <Button className={Classes.MINIMAL} icon="document" text="Files" />
      </NavbarGroup>
      <NavbarGroup align="right">
        <Button className={Classes.MINIMAL} icon="user" />
        <Button className={Classes.MINIMAL} icon="notifications" />
        <Button className={Classes.MINIMAL} icon="cog" />
      </NavbarGroup>
    </Navbar>
  );
};