store = {}
store['timestamp']=1620294924
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/rejection_ood_experiment.py', '--id=2']
store['commit']='2edd2424ec449a84ea20a7324261784a7627b78d'
store['github_url']='2edd2424ec449a84ea20a7324261784a7627b78d'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/rejection_ood_experiment.py'
store['job_id']=2
store['worker_id']=2
store['num_workers']=40
store['config']={'seed': 2, 'acquisition_size': 20, 'max_training_set': 450, 'num_pool_samples': 100, 'num_eval_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'validation_set_size': 1024, 'validation_split_random_state': 0, 'initial_training_set_size': 20, 'samples_per_epoch': 5056, 'mnist_repetitions': 1, 'add_dataset_noise': False, 'acquisition_function': 'batchbald_redux.acquisition_functions.BALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationPoolModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 0.0}
store['log']={}
store['dataset_info']={'training': "(FastMNIST (train; 58976 samples)) + ('OoD Dataset (60000 samples)' | constant_target{'target': tensor(-1, device='cuda:0'), 'num_classes': 10})", 'test': "'FastMNIST (test, 10000 samples)'"}
store['initial_training_set_indices']=[30392, 53434, 12640, 8533, 22304, 37915, 58226, 44119, 3091, 14640, 58125, 39579, 43812, 53689, 52296, 46037, 22015, 40334, 57520, 43803]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 2.334061861038208})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 2.2475953102111816})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 2.51230525970459})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 2.901860237121582})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 2.6361658573150635})
store['active_learning_steps'][0]['training']['best_epoch']=2
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.701, 'crossentropy': 2.23410625}
store['active_learning_steps'][0]['acquisition']={'indices': [1413, 20037, 12202, 3014, 44820, 19981, 8734, 36661, 14122, 42609, 55743, 21155, 36323, 56155, 14373, 44202, 4606, 10255, 23472, 9608], 'labels': [5, 8, 9, 8, 5, 8, 5, 5, 5, 5, 3, 5, 8, 5, 2, 8, 9, 5, 2, 8], 'scores': [1.311108112335205, 1.2904602885246277, 1.2503125071525574, 1.2395075559616089, 1.2392075657844543, 1.2323020696640015, 1.22355455160141, 1.2224423289299011, 1.2179656028747559, 1.20656156539917, 1.2063143849372864, 1.203519582748413, 1.1974134147167206, 1.1893798112869263, 1.1888054609298706, 1.1863840818405151, 1.1838160753250122, 1.1800321340560913, 1.1753073930740356, 1.174397885799408]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 2.066838264465332})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 2.5228707790374756})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 2.4166529178619385})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 2.7086195945739746})
store['active_learning_steps'][1]['training']['best_epoch']=1
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.6383, 'crossentropy': 1.88161484375}
store['active_learning_steps'][1]['acquisition']={'indices': [13667, 10028, 54065, 37084, 26380, 42671, 28313, 12345, 29390, 11096, 32319, 45800, 27915, 21315, 42255, 33388, 58215, 21686, 49580, 34718], 'labels': [2, 9, 7, 2, 9, 2, 9, 3, 9, 9, 3, 9, 2, 8, 3, 8, 2, 9, 2, 2], 'scores': [1.0857871770858765, 1.0681111812591553, 1.062897503376007, 1.0153866410255432, 1.0108659267425537, 1.010170042514801, 0.994468629360199, 0.9938488006591797, 0.9889569878578186, 0.9884409308433533, 0.9857245683670044, 0.9855788946151733, 0.9845257997512817, 0.9818374514579773, 0.9801863431930542, 0.976771354675293, 0.9744096398353577, 0.9742690920829773, 0.9734917283058167, 0.9726046919822693]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 1.5271766185760498})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 2.002941370010376})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 2.0970888137817383})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 2.1929235458374023})
store['active_learning_steps'][2]['training']['best_epoch']=1
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.6921, 'crossentropy': 1.39726904296875}
store['active_learning_steps'][2]['acquisition']={'indices': [49268, 53678, 4535, 21403, 52508, 18538, 7114, 51167, 7855, 36318, 48412, 1828, 34730, 19770, 13074, 36741, 6117, 18645, 6710, 51235], 'labels': [0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0], 'scores': [0.9154679775238037, 0.899196445941925, 0.8572197556495667, 0.8566538691520691, 0.8526453971862793, 0.8525663018226624, 0.8512094616889954, 0.8507615327835083, 0.8485538959503174, 0.8419461846351624, 0.8414536118507385, 0.8367177248001099, 0.8282026052474976, 0.8278847932815552, 0.8267108201980591, 0.8161462545394897, 0.8114823698997498, 0.8107427954673767, 0.8090223073959351, 0.8088677525520325]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 1.7810494899749756})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 2.2810750007629395})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 2.6639389991760254})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 2.8708434104919434})
store['active_learning_steps'][3]['training']['best_epoch']=1
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.646, 'crossentropy': 1.67288984375}
store['active_learning_steps'][3]['acquisition']={'indices': [49026, 39663, 23468, 29853, 2738, 39451, 4646, 24010, 39726, 12959, 28366, 21451, 13215, 44414, 39597, 17129, 46439, 52049, 2519, 35882], 'labels': [6, 2, 2, 2, 2, 1, 2, 2, 2, 6, 2, 2, 0, 2, 2, 1, 0, 6, 6, 2], 'scores': [0.8754252195358276, 0.8554601669311523, 0.8303297758102417, 0.8221957683563232, 0.8089988231658936, 0.8088274002075195, 0.8061282634735107, 0.8055134415626526, 0.8045020699501038, 0.8031903505325317, 0.8030868768692017, 0.7988145351409912, 0.7942719459533691, 0.79231858253479, 0.7884074449539185, 0.7863141298294067, 0.7849181294441223, 0.7844072580337524, 0.779397189617157, 0.7730798721313477]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 1.224466323852539})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7373046875, 'crossentropy': 1.3553926944732666})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.74609375, 'crossentropy': 1.6626949310302734})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7529296875, 'crossentropy': 1.63307523727417})
store['active_learning_steps'][4]['training']['best_epoch']=1
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.724, 'crossentropy': 1.2143990234375}
store['active_learning_steps'][4]['acquisition']={'indices': [4723, 4761, 46476, 11154, 48372, 14020, 45118, 7354, 23104, 38898, 47140, 49202, 12986, 5748, 43126, 6418, 30896, 2209, 32659, 49760], 'labels': [5, 8, 5, 5, 8, 8, 5, 5, 0, 4, 3, 5, 5, 3, 3, 5, 5, 5, 5, 5], 'scores': [0.7441836595535278, 0.740892767906189, 0.7233911752700806, 0.7149159908294678, 0.7083462476730347, 0.7073286771774292, 0.705784261226654, 0.7056928873062134, 0.7019145488739014, 0.7004020810127258, 0.7001489400863647, 0.6996076703071594, 0.6992555856704712, 0.6963678598403931, 0.6947321891784668, 0.6933189630508423, 0.6925746202468872, 0.6923540234565735, 0.6919062733650208, 0.6877912282943726]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 1.3398405313491821})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7509765625, 'crossentropy': 1.2993240356445312})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7509765625, 'crossentropy': 1.4836795330047607})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.744140625, 'crossentropy': 1.7426680326461792})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 2.020035982131958})
store['active_learning_steps'][5]['training']['best_epoch']=2
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.7728, 'crossentropy': 1.17297763671875}
store['active_learning_steps'][5]['acquisition']={'indices': [26444, 35051, 37769, 5968, 193, 37974, 47089, 20996, 17399, 6650, 942, 8353, 15510, 7833, 27542, 25309, 31761, 34429, 52358, 11647], 'labels': [1, 2, 7, 7, 7, 2, 4, 7, 4, 7, 7, 7, 2, 5, 7, 2, 4, 4, 2, 9], 'scores': [0.9193903803825378, 0.900037407875061, 0.894633412361145, 0.8922863602638245, 0.8920357823371887, 0.891511082649231, 0.881006121635437, 0.8776406645774841, 0.876197338104248, 0.8740357756614685, 0.8736495971679688, 0.8705256581306458, 0.8605673313140869, 0.8595373034477234, 0.8569454550743103, 0.852480411529541, 0.8508039712905884, 0.8489954471588135, 0.8484491109848022, 0.8456690311431885]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7392578125, 'crossentropy': 1.151376485824585})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 1.042311191558838})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 1.132056474685669})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 1.2147109508514404})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 1.1906031370162964})
store['active_learning_steps'][6]['training']['best_epoch']=2
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.8179, 'crossentropy': 0.9528322265625}
store['active_learning_steps'][6]['acquisition']={'indices': [31063, 57972, 33593, 11257, 27335, 14335, 39656, 125, 42787, 34789, 28512, 28102, 14277, 40766, 18713, 16860, 46832, 27898, 3791, 4909], 'labels': [2, 4, 2, 2, 4, 4, 0, -1, 4, 2, 5, 0, 7, 4, 2, 8, 7, 2, 2, 8], 'scores': [0.9485164880752563, 0.9353755116462708, 0.9182347655296326, 0.9064795970916748, 0.8983432650566101, 0.8926641941070557, 0.8861332535743713, 0.8834672570228577, 0.8748974800109863, 0.8725215196609497, 0.8616683483123779, 0.858346164226532, 0.8571059107780457, 0.8541410565376282, 0.8536588549613953, 0.8522084951400757, 0.8514237999916077, 0.8454278707504272, 0.8440766930580139, 0.8431582450866699]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7333984375, 'crossentropy': 1.1611405611038208})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.8662415742874146})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.9284021854400635})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.9495443105697632})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.9788209199905396})
store['active_learning_steps'][7]['training']['best_epoch']=2
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.857, 'crossentropy': 0.7772072265625}
store['active_learning_steps'][7]['acquisition']={'indices': [35566, 20113, 2856, 17542, 36286, 7919, 26184, 24533, 44345, 34578, 22634, 19276, 18279, 15891, 10746, 28373, 15276, 29611, 40130, 55278], 'labels': [6, 6, 4, 6, 4, 4, 0, 8, 4, 6, 0, 6, 4, 4, 9, 4, 7, 2, 4, 0], 'scores': [0.8528591990470886, 0.8264074921607971, 0.8262863755226135, 0.8240935206413269, 0.8183349370956421, 0.8053790926933289, 0.8045937418937683, 0.8033603429794312, 0.8010884523391724, 0.800998330116272, 0.7972065210342407, 0.7930274605751038, 0.7896292805671692, 0.7783398628234863, 0.7768828868865967, 0.7750305533409119, 0.7745994329452515, 0.7738828659057617, 0.7735311985015869, 0.7732456922531128]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.74609375, 'crossentropy': 1.1399903297424316})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.8679789304733276})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 0.891636848449707})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.936981201171875})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.9633252620697021})
store['active_learning_steps'][8]['training']['best_epoch']=2
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.8801, 'crossentropy': 0.70607294921875}
store['active_learning_steps'][8]['acquisition']={'indices': [46329, 21023, 11202, 32519, 3810, 33812, 27783, 57876, 30144, 53872, 16379, 424, 18739, 52462, 27429, 32776, 20322, 46412, 33760, 46068], 'labels': [3, 2, 9, 5, 3, 6, 3, 2, 9, 8, 7, 9, 3, 9, 0, 4, 1, 0, 3, 3], 'scores': [0.9165359735488892, 0.8470602631568909, 0.8312305212020874, 0.8303622603416443, 0.8303132057189941, 0.821208119392395, 0.8167906403541565, 0.8154624700546265, 0.8032078742980957, 0.8018280267715454, 0.7993949055671692, 0.799300491809845, 0.7985296249389648, 0.7962433099746704, 0.7949931621551514, 0.7925347089767456, 0.7913310527801514, 0.7889004945755005, 0.7870821952819824, 0.784582257270813]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7294921875, 'crossentropy': 1.1392600536346436})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 0.8482253551483154})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.8509345650672913})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.7430386543273926})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.7929450869560242})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.9166367053985596})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.9916620850563049})
store['active_learning_steps'][9]['training']['best_epoch']=4
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.8949, 'crossentropy': 0.650815234375}
store['active_learning_steps'][9]['acquisition']={'indices': [42703, 11822, 18671, 25644, 12188, 1652, 18398, 57728, 34445, 49364, 15949, 49013, 46557, 50320, 20183, 22480, 30156, 42363, 35401, 1518], 'labels': [0, 7, 7, 4, 7, 7, 4, 9, 7, 7, 5, 0, 0, 5, 4, 4, 0, 7, 3, 9], 'scores': [1.0518588423728943, 0.9828353524208069, 0.9809681177139282, 0.9644383788108826, 0.9400395750999451, 0.9197266697883606, 0.9190700650215149, 0.9165226221084595, 0.9119038879871368, 0.9020079374313354, 0.901340663433075, 0.9003376960754395, 0.8976132273674011, 0.8964922428131104, 0.8948220014572144, 0.8912514448165894, 0.8909319639205933, 0.8908594846725464, 0.8877147436141968, 0.8871427178382874]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.791015625, 'crossentropy': 1.013677716255188})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.6935564875602722})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.7078306674957275})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6490951776504517})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6970313787460327})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.7163733839988708})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.797180712223053})
store['active_learning_steps'][10]['training']['best_epoch']=4
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.9161, 'crossentropy': 0.54693671875}
store['active_learning_steps'][10]['acquisition']={'indices': [1075, 4153, 36744, 18487, 20172, 32355, 52889, 50459, 42415, 49088, 36818, 14749, 13928, 48360, 40169, 41933, 18150, 39419, 2728, 26358], 'labels': [7, 2, 1, 4, 4, 8, -1, 8, 7, 8, 7, 0, 2, 3, 4, 5, 8, 8, 9, 3], 'scores': [1.00529944896698, 1.0005701780319214, 0.9719842076301575, 0.9504806399345398, 0.9499766230583191, 0.9495641589164734, 0.938683271408081, 0.9197402596473694, 0.9177395105361938, 0.9137322902679443, 0.8929895162582397, 0.8925936222076416, 0.8921961188316345, 0.8904538154602051, 0.8878023624420166, 0.8835880756378174, 0.8759849071502686, 0.8757615685462952, 0.8755089044570923, 0.8727557063102722]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 1.160430669784546})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.7120263576507568})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6612262725830078})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.727986216545105})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.596390962600708})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6146351099014282})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.7480517625808716})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6488034725189209})
store['active_learning_steps'][11]['training']['best_epoch']=5
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.9305, 'crossentropy': 0.49500234375}
store['active_learning_steps'][11]['acquisition']={'indices': [31301, 50461, 20169, 47626, 54858, 52889, 31184, 45026, 1674, 20855, 5842, 52169, 3910, 24753, 16628, 52478, 34024, 24687, 33505, 45822], 'labels': [5, 7, 4, -1, 3, -1, 9, 8, 9, 6, 1, 2, 6, 6, 9, 9, 6, 6, 2, -1], 'scores': [1.119755506515503, 1.0364571809768677, 1.012803316116333, 1.0043349862098694, 0.9758978486061096, 0.9705482125282288, 0.9507260918617249, 0.9486502408981323, 0.9472126960754395, 0.9460338354110718, 0.9446447491645813, 0.9433454871177673, 0.9428818821907043, 0.941989541053772, 0.9411345720291138, 0.9377934336662292, 0.9373844265937805, 0.9339821934700012, 0.9330019950866699, 0.9274698495864868]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.7724609375, 'crossentropy': 1.0582826137542725})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6301722526550293})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5787968039512634})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5230787992477417})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5408252477645874})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5706368088722229})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5504328012466431})
store['active_learning_steps'][12]['training']['best_epoch']=4
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.94, 'crossentropy': 0.46157197265625}
store['active_learning_steps'][12]['acquisition']={'indices': [34328, 52910, 52686, 20050, 50370, 49563, 20641, 47885, 48356, 7782, 2633, 9390, 56414, 37048, 12663, 15779, 50403, 9966, 36417, 17941], 'labels': [8, 9, 5, 9, 7, 8, 9, 9, 2, 2, 9, 9, -1, 9, 8, 0, -1, 0, 6, 0], 'scores': [0.8856086730957031, 0.8740065693855286, 0.8669645190238953, 0.8655179738998413, 0.8638920187950134, 0.8467977046966553, 0.8390920758247375, 0.8333661556243896, 0.8326833248138428, 0.8308244347572327, 0.8252418041229248, 0.8247390985488892, 0.8246312141418457, 0.8230378031730652, 0.8228846192359924, 0.8210970759391785, 0.8204811811447144, 0.8196288347244263, 0.8137618899345398, 0.8127405047416687]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 1.0298899412155151})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6801013946533203})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5921027660369873})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5604724884033203})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5381316542625427})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.523998498916626})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5271925330162048})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5518465042114258})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.564866304397583})
store['active_learning_steps'][13]['training']['best_epoch']=6
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.937, 'crossentropy': 0.464450537109375}
store['active_learning_steps'][13]['acquisition']={'indices': [5013, 31014, 24424, 57342, 35606, 11569, 59297, 52771, 44149, 12305, 39818, 10992, 29018, 9180, 20171, 49515, 6347, 30451, 3486, 52407], 'labels': [2, 8, 1, 2, 2, 5, 1, 3, 2, 9, 1, -1, -1, 3, 5, 2, 3, 8, -1, -1], 'scores': [1.0475723147392273, 1.0144875645637512, 0.9884555339813232, 0.9830589890480042, 0.9681304693222046, 0.9611411094665527, 0.9539321064949036, 0.9478613138198853, 0.9475992321968079, 0.933125376701355, 0.9324086904525757, 0.9314661026000977, 0.9302462935447693, 0.9285290837287903, 0.9214443564414978, 0.9202725291252136, 0.9188103675842285, 0.9139931797981262, 0.9116459488868713, 0.9115055799484253]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 1.1449365615844727})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6260057687759399})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5591152310371399})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5075979828834534})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5203104615211487})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.519881010055542})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.4708878993988037})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5160562992095947})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.4801298975944519})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5693044662475586})
store['active_learning_steps'][14]['training']['best_epoch']=7
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.9454, 'crossentropy': 0.4139642578125}
store['active_learning_steps'][14]['acquisition']={'indices': [24479, 52889, 15855, 55778, 36508, 14697, 37275, 11693, 56006, 17518, 52697, 31664, 48638, 59980, 47955, 13021, 54994, 19868, 5255, 14935], 'labels': [8, -1, 5, -1, 5, 8, 5, 3, 3, 0, 3, 3, 0, 3, 5, 5, 6, 5, 5, 3], 'scores': [1.0704774260520935, 1.0556761622428894, 1.0385212898254395, 1.0180587768554688, 1.0136983394622803, 0.9845933318138123, 0.9826438426971436, 0.9773070812225342, 0.964279294013977, 0.9635419845581055, 0.9570071697235107, 0.9515515565872192, 0.9491164088249207, 0.9487180709838867, 0.9454407095909119, 0.9443386197090149, 0.9439736008644104, 0.9375467300415039, 0.93635493516922, 0.9358025789260864]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.7626953125, 'crossentropy': 1.1731890439987183})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.7552748322486877})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5576644539833069})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5192033648490906})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.5880013704299927})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5489636659622192})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5396329164505005})
store['active_learning_steps'][15]['training']['best_epoch']=4
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.9346, 'crossentropy': 0.48443056640625}
store['active_learning_steps'][15]['acquisition']={'indices': [30884, 11292, 54814, 50618, 2148, 6466, 37696, 3794, 7325, 47278, 59747, 45944, 59314, 26618, 48407, 30588, 17739, 31090, 5789, 24462], 'labels': [2, 1, 4, 6, 6, 2, 2, 6, 0, 5, 5, 9, 9, 4, 8, 4, 5, 4, -1, 2], 'scores': [0.8698365092277527, 0.8644877672195435, 0.8532449007034302, 0.8446596264839172, 0.8361411094665527, 0.8359476327896118, 0.8342432975769043, 0.8145069479942322, 0.8111371994018555, 0.8109568357467651, 0.8102091550827026, 0.8096212148666382, 0.8085945248603821, 0.8070498108863831, 0.8045654296875, 0.8012975454330444, 0.8002819418907166, 0.7988280057907104, 0.7940937280654907, 0.7935138940811157]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.7685546875, 'crossentropy': 1.1677725315093994})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.625184953212738})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5589468479156494})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5032097101211548})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.4887639284133911})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.555406928062439})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4947860836982727})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.4893079996109009})
store['active_learning_steps'][16]['training']['best_epoch']=5
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.9439, 'crossentropy': 0.444157763671875}
store['active_learning_steps'][16]['acquisition']={'indices': [22083, 49889, 34847, 48006, 52889, 21426, 4004, 50736, 42973, 37672, 11648, 46658, 17265, 1573, 47626, 19590, 9439, 26079, 22272, 40066], 'labels': [2, 0, 0, 6, -1, 6, 5, -1, 4, 8, 2, 8, 2, 2, -1, 5, 0, 8, 5, 4], 'scores': [0.9442899823188782, 0.9078453183174133, 0.8917059302330017, 0.8788328170776367, 0.8726952075958252, 0.8634020090103149, 0.858370840549469, 0.854910135269165, 0.8535921573638916, 0.8410990834236145, 0.83774733543396, 0.8329173922538757, 0.8321253657341003, 0.8317478895187378, 0.8305720686912537, 0.8217253684997559, 0.8184252381324768, 0.8130214810371399, 0.8070152997970581, 0.8053133487701416]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.779296875, 'crossentropy': 1.1829509735107422})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.6456723213195801})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5361853837966919})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.4426805377006531})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4172343909740448})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4510647654533386})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4493125379085541})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.49414074420928955})
store['active_learning_steps'][17]['training']['best_epoch']=5
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.9506, 'crossentropy': 0.37873974609375}
store['active_learning_steps'][17]['acquisition']={'indices': [32880, 50840, 41453, 10350, 18003, 40624, 36704, 47626, 14700, 33301, 36126, 59286, 55314, 5600, 34771, 1423, 49910, 2782, 4822, 5536], 'labels': [0, 2, 3, -1, 2, -1, 2, -1, -1, -1, 5, 8, 6, 6, 0, 0, 6, -1, 4, 8], 'scores': [0.8988375663757324, 0.8775142431259155, 0.8694585561752319, 0.8614521026611328, 0.8508830070495605, 0.8430385589599609, 0.8389421701431274, 0.825522780418396, 0.8245628476142883, 0.8221800923347473, 0.8200644850730896, 0.8147173523902893, 0.809358537197113, 0.802622377872467, 0.8019166588783264, 0.7979870438575745, 0.7954292893409729, 0.7905551195144653, 0.7902923822402954, 0.7895687222480774]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 1.3970212936401367})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.7265190482139587})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5753316283226013})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.4773097634315491})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4793418049812317})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.46246838569641113})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.46064308285713196})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.4668068289756775})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.48046404123306274})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4542006850242615})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4699530601501465})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.49239248037338257})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.4283290505409241})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4865448474884033})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.529420018196106})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.47203636169433594})
store['active_learning_steps'][18]['training']['best_epoch']=13
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.9511, 'crossentropy': 0.4086731201171875}
store['active_learning_steps'][18]['acquisition']={'indices': [49573, 41924, 39208, 36450, 52889, 55778, 32747, 5443, 41371, 37583, 23578, 14201, 13942, 32276, 7949, 340, 8978, 7478, 54950, 8300], 'labels': [2, 9, 5, 2, -1, -1, 8, -1, 0, -1, 2, 7, 4, 3, -1, 7, 2, 9, 8, 8], 'scores': [1.1352607607841492, 1.0636098980903625, 1.0536190867424011, 1.048649936914444, 1.0451642870903015, 1.0341734290122986, 1.0312623977661133, 1.001105010509491, 0.9946879148483276, 0.9936284422874451, 0.9731036424636841, 0.9718660116195679, 0.9697244763374329, 0.9600828289985657, 0.9590460062026978, 0.9588518738746643, 0.958622545003891, 0.9569460153579712, 0.9528148174285889, 0.9505478739738464]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.7275390625, 'crossentropy': 1.2537176609039307})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5937141180038452})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4947776794433594})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.3926777243614197})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.396548867225647})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.40811294317245483})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.3601243197917938})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.43230366706848145})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.41984155774116516})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4362974166870117})
store['active_learning_steps'][19]['training']['best_epoch']=7
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.9541, 'crossentropy': 0.3454376953125}
store['active_learning_steps'][19]['acquisition']={'indices': [52889, 29376, 49890, 32638, 33153, 5789, 39164, 39778, 43235, 18130, 4379, 24404, 12321, 5298, 26738, 8865, 50371, 39355, 41578, 42428], 'labels': [-1, -1, 5, -1, 7, -1, -1, 8, -1, 8, -1, -1, 0, 0, 4, 3, 7, -1, 8, 5], 'scores': [0.9243875741958618, 0.9053911566734314, 0.8989830017089844, 0.895032525062561, 0.8691877722740173, 0.8663007020950317, 0.8592677712440491, 0.8584222197532654, 0.857205867767334, 0.8526211977005005, 0.8500586152076721, 0.8496072888374329, 0.8452111482620239, 0.8416222333908081, 0.8416023850440979, 0.8356326818466187, 0.8312328457832336, 0.8290168046951294, 0.8288545608520508, 0.8244422674179077]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 1.297775387763977})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6743514537811279})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.5111211538314819})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.41926270723342896})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4355480670928955})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3782474398612976})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.41949206590652466})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3776698708534241})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4420342445373535})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.40421855449676514})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4229546785354614})
store['active_learning_steps'][20]['training']['best_epoch']=8
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.9582, 'crossentropy': 0.35601865234375}
store['active_learning_steps'][20]['acquisition']={'indices': [54097, 8668, 34188, 45602, 52889, 59099, 10149, 54969, 52163, 4379, 56662, 52422, 6474, 13845, 53990, 10044, 49505, 40976, 16756, 22597], 'labels': [7, 5, 3, 5, -1, -1, 6, 6, 6, -1, 0, 2, 6, 6, -1, 6, 6, 1, 7, 9], 'scores': [0.9330956339836121, 0.9274664521217346, 0.9248767495155334, 0.9142979383468628, 0.9131879210472107, 0.9074721336364746, 0.9055567383766174, 0.9028496146202087, 0.9025588631629944, 0.9021197557449341, 0.901481032371521, 0.898890495300293, 0.8953500986099243, 0.8952736854553223, 0.8913725018501282, 0.8890011608600616, 0.8838561177253723, 0.8781635761260986, 0.8773797750473022, 0.8763062357902527]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 1.3088840246200562})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.7209888696670532})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4946078062057495})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.4512455463409424})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.4072122871875763})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.38083499670028687})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.39303603768348694})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3784738779067993})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3654952943325043})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3676537573337555})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.38209882378578186})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.4324282705783844})
store['active_learning_steps'][21]['training']['best_epoch']=9
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.9555, 'crossentropy': 0.369434765625}
store['active_learning_steps'][21]['acquisition']={'indices': [29018, 45171, 55778, 6512, 10181, 20636, 49354, 16226, 50249, 38912, 38052, 46975, 7949, 24860, 4955, 7308, 32823, 8704, 29376, 13998], 'labels': [-1, -1, -1, -1, -1, 9, 0, -1, -1, -1, 4, -1, -1, 9, 2, 8, -1, 1, -1, 9], 'scores': [1.0242149829864502, 1.0208048224449158, 1.0143404006958008, 0.9977052807807922, 0.9954520463943481, 0.9805537462234497, 0.9741420745849609, 0.9710448980331421, 0.9588277339935303, 0.9390844106674194, 0.937699019908905, 0.9341476559638977, 0.9303693771362305, 0.927566409111023, 0.9248762130737305, 0.9235715866088867, 0.921887993812561, 0.917815089225769, 0.9172770977020264, 0.9151690602302551]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 1.2047581672668457})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6709754467010498})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5398176908493042})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.40116655826568604})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.39495769143104553})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3519684970378876})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3970237970352173})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3728770315647125})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.34814590215682983})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.36509793996810913})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.38494980335235596})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.37707340717315674})
store['active_learning_steps'][22]['training']['best_epoch']=9
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.9614, 'crossentropy': 0.3319337158203125}
store['active_learning_steps'][22]['acquisition']={'indices': [52889, 39355, 18324, 57311, 48102, 49487, 44661, 18598, 5295, 31284, 38920, 58832, 36990, 23112, 41334, 24630, 53990, 52834, 49002, 53054], 'labels': [-1, 8, 0, 5, 7, 8, 1, 9, 4, 7, 7, 3, -1, 8, 9, 5, -1, 2, 1, -1], 'scores': [0.9372084140777588, 0.9103165864944458, 0.9091691374778748, 0.9061664938926697, 0.9038549661636353, 0.9037452936172485, 0.9028725624084473, 0.9006215333938599, 0.8998674154281616, 0.8985627889633179, 0.8959962129592896, 0.8884910345077515, 0.8820205330848694, 0.8814116418361664, 0.8765242099761963, 0.874697208404541, 0.8734694123268127, 0.8734331130981445, 0.8721057176589966, 0.8708401322364807]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.7646484375, 'crossentropy': 1.1922898292541504})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.7186692953109741})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.5161553025245667})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.41510939598083496})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.41275471448898315})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.4133896827697754})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3786660432815552})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.36970609426498413})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.365226686000824})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.35631605982780457})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.41103166341781616})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3839523196220398})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.40398740768432617})
store['active_learning_steps'][23]['training']['best_epoch']=10
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.9618, 'crossentropy': 0.3471245361328125}
store['active_learning_steps'][23]['acquisition']={'indices': [24263, 635, 52937, 31512, 30177, 20110, 49543, 52914, 32668, 57300, 43745, 34665, 5315, 34828, 19089, 51863, 45911, 56183, 56196, 27576], 'labels': [9, 5, 7, 2, 7, 4, 8, 5, 9, 3, 8, 9, 3, -1, 5, 9, 3, 4, -1, 5], 'scores': [1.0412498712539673, 1.0256941318511963, 1.0138984322547913, 1.0029661059379578, 0.998977780342102, 0.9781982600688934, 0.9755864143371582, 0.9666673541069031, 0.9621309638023376, 0.9604540467262268, 0.9483155012130737, 0.9473644495010376, 0.9412002563476562, 0.935623288154602, 0.9352323412895203, 0.9324369430541992, 0.9322493672370911, 0.929180920124054, 0.9267529845237732, 0.9258254170417786]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.716796875, 'crossentropy': 1.2781264781951904})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.6494905948638916})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.5118327140808105})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.4319404363632202})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3611548840999603})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.34153807163238525})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3715065121650696})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3660014271736145})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.32841479778289795})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3345021903514862})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3280068635940552})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.33781999349594116})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.34673118591308594})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.32595980167388916})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.36257126927375793})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.33462226390838623})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.36592215299606323})
store['active_learning_steps'][24]['training']['best_epoch']=14
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.9673, 'crossentropy': 0.3026446533203125}
store['active_learning_steps'][24]['acquisition']={'indices': [30851, 13969, 39561, 26266, 42438, 52889, 26882, 15723, 34946, 56196, 41612, 15699, 53844, 4379, 40378, 1254, 59726, 40530, 8116, 17958], 'labels': [-1, 3, 2, 7, 9, -1, 7, 8, 8, -1, 0, 2, 5, -1, -1, -1, -1, 2, 0, 9], 'scores': [1.0771392583847046, 1.0424659252166748, 1.0409129858016968, 1.0306191444396973, 1.0013816356658936, 1.000657320022583, 0.9835909903049469, 0.9667206406593323, 0.9617976546287537, 0.9562687873840332, 0.9547487497329712, 0.9547401070594788, 0.9531939625740051, 0.9526839852333069, 0.9405195116996765, 0.9393982887268066, 0.9393407106399536, 0.9379422664642334, 0.9329831004142761, 0.9290078282356262]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.7236328125, 'crossentropy': 1.3979133367538452})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.7567152976989746})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.5242898464202881})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.522625744342804})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.36203908920288086})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3933667540550232})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3515315055847168})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.3487178683280945})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3325575292110443})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.34025055170059204})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.37676405906677246})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.34237802028656006})
store['active_learning_steps'][25]['training']['best_epoch']=9
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.962, 'crossentropy': 0.353363671875}
