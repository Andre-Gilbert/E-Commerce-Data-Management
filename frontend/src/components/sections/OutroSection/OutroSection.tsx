/** The outro section of the landing page. */
import { Classes } from '@blueprintjs/core';
import { GradientBackgroundSection } from '../GradientBackgroundSection/GradientBackgroundSection';
import { SignInButton } from '../../buttons/SignInButton/SignInButton';
import { SignUpButton } from '../../buttons/SignUpButton/SignUpButton';
import { Wrapper, Grid, Title, Subtitle, ButtonWrapper } from './styles';

export const OutroSection = () => {
  return (
    <GradientBackgroundSection curveFlipX={true}>
      <Wrapper>
        <Grid>
          <Title className={Classes.DARK}>Get Started Now.</Title>
          <Subtitle className={Classes.DARK}>
            We build world-class software for data analytics and data-driven
            decision making.
          </Subtitle>
          <ButtonWrapper>
            <SignInButton />
            <SignUpButton />
          </ButtonWrapper>
        </Grid>
      </Wrapper>
    </GradientBackgroundSection>
  );
};