/*
Copyright 2020 The Magma Authors.

This source code is licensed under the BSD-style license found in the
LICENSE file in the root directory of this source tree.

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
*/

#pragma once
#ifdef __cplusplus
extern "C" {
#endif
#include "intertask_interface.h"
#include "common_types.h"
void send_s8_create_session_request(
    teid_t sgw_s11_teid, const itti_s11_create_session_request_t* msg,
    imsi64_t imsi64);
#ifdef __cplusplus
}
#endif
