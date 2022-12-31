import subprocess

input_file = "input.mp4"
gifs = [
 ("A.1a-adv", 60*4+1.5, 5.8),
 ("A.1a-beg", 60*4+10, 8),
 ("A.1b", 60*4+25.4, 7),
 ("A.1c", 60*4+49.25, 4.65),
 ("A.2a-adv", 60*5+16.5, 5.5),
 ("A.2a-beg", 60*5+22.6, 8.8),
 ("A.2b-adv", 60*5+35.5, 7),
 ("A.2b-beg", 60*5+52, 6),
 ("A.2c-adv", 60*5+61, 8),
 ("A.2c-beg", 60*6+11, 5.8),
 ("A.3a-adv", 60*6+25, 11),
 ("A.3a-beg", 60*6+39.3, 7.6),
 ("A.3b", 60*6+50.6, 10.9),
 ("A.3c-adv", 60*7+5.5, 11.2),
 ("A.3c-beg", 60*7+18.5, 4.8),
 ("A.4a-adv", 60*7+29, 9.5),
 ("A.4a-beg", 60*7+40.5, 9.3),
 ("A.4b-adv", 60*7+54.4, 13),
 ("A.4b-beg", 60*8+32, 12.6),
 ("A.4c", 60*8+47, 8.8),
 ("A.5a", 60*9+3.2, 10.5),
 ("A.5b", 60*9+16.4, 14),
 ("A.5c", 60*9+34, 7.4),
 ("A.6", 60*9+52.5, 22),
 ("B.1a", 60*10+42.8, 15.2),
 ("B.1b", 60*11+13, 8.8),
 ("B.1c", 60*11+36, 6),
 ("B.2a-adv", 60*11+56.2, 22, False),  # no boomerang, decrease in difficulty
 ("B.2a-beg", 60*12+23.4, 7, False),  # same
 ("B.2b-adv", 60*12+35.5, 14.3),
 ("B.2b-beg", 60*12+57, 2.5),
 ("B.2c", 60*13+9, 8.6),
 ("B.3a", 60*13+27.5, 14.3),
 ("B.3b", 60*13+46.3, 3.7),
 ("B.3c", 60*14+2.6, 4.6),
 ("B.4a-adv", 60*14+16.1, 5.4),
 ("B.4a-beg", 60*14+26.6, 4.1),
 ("B.4b", 60*14+32.4, 12.1),
 ("B.4c", 60*14+50.4, 9),
 ("B.5a", 60*15+9.5, 6.1),
 ("B.5b", 60*15+21.8, 5.5),
 ("B.5c", 60*15+30, 6.5),
 ("B.6", 60*15+41.6, 8),  # quick up, slow down?
]
do_only_one = 28

#
# Define/test ffmpeg filters
#

# When you forget "split", e.g. in the following:
#     test = "[0]scale=320:-1[s0];[s0]reverse[r];[s0][r]concat=n=2:v=1:a=0,fps=8"
# the error should say:
#     [s0] is already connecting from "scale=320:-1" to "reverse" and cannot also connect to "concat=n=2:v=1:a=0,fps=8"

# Some palette setting option - useful for GIFs:
# palette = "[s0]palettegen[p];[s1][p]paletteuse"
# palette = "[s0]palettegen=max_colors=32[p];[s1][p]paletteuse=dither=bayer"
# decrease_palette_for_gif=",split[p0][p1];[p0]palettegen[p];[p1][p]paletteuse"

#scale = "fps=8,scale=320:-1:flags=lanczos"
#boomerang = "[0]scale=320:-1,reverse[r];[0]scale=320:-1,[r]concat=n=2:v=1:a=0,fps=8"
# Boomerang + pallet
#boomerang = "[0]scale=320:-1,fps=8,split[p0][p1];[p0]palettegen[p];[p1][p]paletteuse"

# boomerangs with single-frame precision using trim
#boomerang_trim = "[0]scale=320:-1,trim=start_frame=1:end_frame=29,setpts=PTS-STARTPTS,split[s0][s1];[s1]reverse[r];[s0][r]concat=n=2:v=1:a=0,split[p0][p1];[p0]palettegen[p];[p1][p]paletteuse"
# no trim
full_filter = "[0]fps=8,scale=320:-1:flags=lanczos,split[s0][s1];[s1]reverse[r];[s0][r]concat=n=2:v=1:a=0,hue=s=0"
half_filter = "[0]fps=8,scale=320:-1:flags=lanczos,hue=s=0"

# Grayscale:
# format=gray
# hue=s=0

#
# Try sketch effect
#full_filter = """
#[0]fps=8,scale=320:-1:flags=lanczos,split[s0][s1];
#[s1]reverse[r];
#[s0][r]concat=n=2:v=1:a=0,format=gray,split[back][gray];
#[gray]negate,gblur=10[front];
#[front][back]blend=all_mode=dodge"""

#edgedetect=enable=1

#full_filter = """
#[0]fps=8,scale=320:-1:flags=lanczos,split[s0][s1];
#[s1]reverse[r];
#[s0][r]concat=n=2:v=1:a=0,format=gray,split=3[back][gray][ovl_pre];
#[gray]negate,gblur=10[front];
#[front][back]blend=all_mode=dodge[ovl_back];
#[ovl_pre]edgedetect=enable=1,negate,format=rgba,colorchannelmixer=ar=-0.33:ag=-0.33:ab=-0.33:aa=0.8[ovl_front];
#[ovl_back][ovl_front]overlay
#"""

# [ovl_pre]edgedetect=enable=1,negate,split[ovl_edge][ovl_tr_pre];
# [ovl_pre]edgedetect=enable=1,negate,format=rgba,colorchannelmixer=aa=0.3[ovl_front];

# [ovl_edge][ovl_tr_pre]alphamerge,format=rgba,colorchannelmixer=aa=0.3[ovl_front];
# [ovl_edge][ovl_tr_pre]alphamerge[ovl_front];


#format=rgba,colorchannelmixer=aa=0.7

#[front][back]blend=all_mode='overlay':all_opacity=0.1"""

#full_filter = "[0]fps=8,scale=320:-1:flags=lanczos,split[s0][s1];[s1]reverse[r];[s0][r]concat=n=2:v=1:a=0,format=gray,edgedetect=enable=1"
#edgedetect=enable='gt(mod(t,60),57)'

#full_filter = "[0]fps=8,scale=320:-1:flags=lanczos,split[s0][s1];[s1]reverse[r];[s0][r]concat=n=2:v=1:a=0,format=gray,edgedetect=enable=1,negate"


#
# Crossfade first and last few seconds
# https://stackoverflow.com/questions/38186672/ffmpeg-make-a-seamless-loop-with-a-crossfade
# fade_sec = 0.2
# crossfade = """[0]split[body][pre];
# [pre]trim=duration='{fade_sec}',format=yuva420p,fade=d='{fade_sec}':alpha=1,setpts=PTS+('{diff_sec}'/TB)[jt];
# [body]trim='{fade_sec}',setpts=PTS-STARTPTS[main];
# [main][jt]overlay"""

#
# Final ffmpeg command
#

ffmpeg_cmd = [
    "ffmpeg",
    "-y",  # Always overwrite output file
    "-ss", "{start_sec}",  # Skip to seconds
    "-t", "{len_sec}",  # Extract this length of time from input
    "-i", "{input_file}",  # Input file
    # fps, scale=width x auto
    #"-vf", f"{scale},split[s0][s1];{palette}",
    #"-vf", f"{scale}"
    "-filter_complex", "{filter}",
    "-an",  # Disable any audio streams in output
    "-loop", "0",  # Create GIF that loops infinitely (-1 = never, 0 = always, >0 = n+1 times)
    "{output_file}.webm",  # Output file (webp over gif for better compression, e.g. duplicated frames)
]

for idx, gif in enumerate(gifs):
    if do_only_one is not None and idx != do_only_one:
        continue
    boomerang = True
    if len(gif) == 3:
        gif = (*gif, boomerang)
    name, start_sec, len_sec, boomerang = gif
    print(name)
    cmd = [arg.format(
        input_file=input_file,
        start_sec=start_sec,
        len_sec=len_sec,
        filter=full_filter if boomerang else half_filter,
        # fade_sec=fade_sec,
        # diff_sec=len_sec - fade_sec,
        output_file=name) for arg in ffmpeg_cmd]
    print("  ", " ".join(cmd))
    result = subprocess.run(cmd, capture_output=True, text=True)
    # print(result.stderr)
    if result.returncode != 0:
        print(cmd)
        print(result.stdout)
        print(result.stderr)
        exit()
    if idx == do_only_one:
        # f'xdg-open "{output_file}.webp"'
        exit()

