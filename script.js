gsap.to(".nav-sectuin",{
    backgroundColor: "black",
    height:"4rem",
    duration:0.5,
    scrollTrigger:{
        trigger:".nav-sectuin",
        scroller:"body",
        start:"top -10%",
        end:"top -11%",
        scrub:1
    }
})
