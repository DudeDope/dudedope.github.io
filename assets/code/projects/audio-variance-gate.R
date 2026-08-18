# Clean transcription of the variance-gating algorithm documented in the
# project report. It suppresses quiet windows; it is not a general speech
# enhancement system.

suppressPackageStartupMessages(library(tuneR))

arguments <- commandArgs(trailingOnly = TRUE)
if (length(arguments) != 2) {
  stop("usage: Rscript audio-variance-gate.R INPUT.wav OUTPUT.wav")
}

input_path <- arguments[[1]]
output_path <- arguments[[2]]
audio <- readWave(input_path)
amplitude <- audio@left
sample_rate <- audio@samp.rate

window_size <- floor(sample_rate / 10) - 1
if (length(amplitude) <= window_size) {
  stop("audio must be longer than one 0.1-second window")
}

starts <- seq(1, length(amplitude) - window_size, by = 1000)
local_variance <- vapply(
  starts,
  function(start) var(amplitude[start:(start + window_size)]),
  numeric(1)
)

variance_range <- diff(range(local_variance))
if (variance_range == 0) {
  stop("the local variance is constant, so a modal cutoff is undefined")
}

scaled_variance <- 1000 * (local_variance - min(local_variance)) / variance_range
variance_bins <- floor(scaled_variance / 25)
modal_bin <- as.integer(names(which.max(table(variance_bins))))
cutoff <- 25 * (modal_bin + 1) + 1

processed <- amplitude
for (index in seq_along(starts)) {
  sample_indices <- starts[[index]]:(starts[[index]] + window_size)
  if (scaled_variance[[index]] < cutoff) {
    processed[sample_indices] <- 0
  } else if (scaled_variance[[index]] < 1.5 * cutoff) {
    processed[sample_indices] <- processed[sample_indices] / 2
  }
}

output <- audio
output@left <- processed
writeWave(output, output_path)

message(sprintf("modal-bin cutoff: %.1f", cutoff))
