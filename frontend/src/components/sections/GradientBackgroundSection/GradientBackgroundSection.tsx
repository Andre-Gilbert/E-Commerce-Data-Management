/** The gradient background of the hero & outro section. */
import { ReactNode } from 'react';
import Image from 'next/image';
import Curve from '../../../images/curve.svg';
import { Section, ImageWrapper } from './styles';

type GradientBackgroundSectionProps = {
  /**
   * Whether to flip the curve SVG on the x-axis.
   */
  curveFlipX: boolean;
  children: ReactNode;
};

export const GradientBackgroundSection = ({
  curveFlipX,
  children,
}: GradientBackgroundSectionProps) => {
  return (
    <Section>
      {children}
      <ImageWrapper flipX={curveFlipX}>
        <Image src={Curve} alt="Curve" layout="responsive" />
      </ImageWrapper>
    </Section>
  );
};