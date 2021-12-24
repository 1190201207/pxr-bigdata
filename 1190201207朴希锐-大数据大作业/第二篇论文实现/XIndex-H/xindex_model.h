

#include "mkl.h"
#include "mkl_lapacke.h"

#if !defined(XINDEX_MODEL_H)
#define XINDEX_MODEL_H

namespace xindex {

template <class key_t>
class LinearModel {
  typedef std::array<double, key_t::model_key_size()> model_key_t;

 public:
  void prepare(const std::vector<key_t> &keys,
               const std::vector<size_t> &positions);
  void prepare(const typename std::vector<key_t>::const_iterator &keys_begin,
               uint32_t size);
  void prepare_model(const std::vector<double *> &model_key_ptrs,
                     const std::vector<size_t> &positions);
  size_t predict(const key_t &key) const;
  size_t get_error_bound(const std::vector<key_t> &keys,
                         const std::vector<size_t> &positions);
  size_t get_error_bound(
      const typename std::vector<key_t>::const_iterator &keys_begin,
      uint32_t size);

 private:
  std::array<double, key_t::model_key_size() + 1> weights;
};

}  // namespace xindex

#endif  // XINDEX_MODEL_H
